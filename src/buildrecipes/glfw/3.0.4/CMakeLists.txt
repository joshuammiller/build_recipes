CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(glfw_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_glfw glfw/glfw-${glfw_version}.tar.gz
    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

message("Install Dir")
message(${CMAKE_INSTALL_PREFIX})

ExternalProject_add(
    glfw
    URL ${url_glfw}
    PREFIX glfw
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} <SOURCE_DIR> -DBUILD_SHARED_LIBS=OFF
                                                -DGLFW_BUILD_EXAMPLES=OFF
                                                -DGLFW_BUILD_TESTS=OFF
                                                -DGLFW_BUILD_DOCS=OFF
                                                -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
)
