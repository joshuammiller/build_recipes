CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(doubleconversion_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_doubleconversion double-conversion/double-conversion-${doubleconversion_version}.tar.gz
    https://github.com/doubleconversion/doubleconversion/archive/${doubleconversion_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    doubleconversion
    URL ${url_doubleconversion}
    PREFIX doubleconversion
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} <SOURCE_DIR>
                                                -DBUILD_SHARED_LIBS=ON
                                                -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
)
