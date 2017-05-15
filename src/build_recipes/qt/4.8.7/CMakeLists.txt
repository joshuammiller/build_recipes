CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_qt qt/qt-everywhere-opensource-src-${qt_version}.tar.gz
    http://download.qt-project.org/official_releases/qt/4.8/${qt_version}/qt-everywhere-opensource-src-${qt_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    qt
    URL ${url_qt}
    URL_MD5 d990ee66bf7ab0c785589776f35ba6ad
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure -prefix ${CMAKE_INSTALL_PREFIX}
                                    -release -confirm-license
                                    -opensource -no-phonon -no-phonon-backend
                                    -no-webkit -no-openvg
                                    -nomake examples -nomake demos -nomake docs
                                    -optimized-qmake
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
)
