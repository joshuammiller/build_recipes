CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(opensubdiv_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_opensubdiv opensubdiv/opensubdiv-${opensubdiv_version}.tar.gz
    https://github.com/opensubdiv/opensubdiv/archive/${opensubdiv_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    opensubdiv
    URL ${url_opensubdiv}
    PREFIX opensubdiv
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} <SOURCE_DIR>
                                                -DNO_PTEX=1
                                                -DNO_OMP=1
                                                -DNO_DOC=1
                                                -DNO_CUDA=1
                                                -DNO_OPENCL=1
                                                -DNO_CLEW=1
                                                -DNO_TUTORIALS=1
                                                -DNO_REGRESSION=1
                                                -DNO_EXAMPLES=1
                                                -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
                                                -DGLFW_LOCATION=$ENV{REZ_GLFW_ROOT}
                                                -DTBB_LOCATION=$ENV{REZ_TBB_ROOT}
                                                -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
)
