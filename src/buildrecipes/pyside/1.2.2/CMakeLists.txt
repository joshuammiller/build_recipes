CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(pyside_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(shiboken_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(tools_version 0.2.15)

rez_set_archive(
	url_pyside pyside/PySide-${pyside_version}.tar.gz
	https://github.com/pyside/PySide/archive/${pyside_version}.tar.gz
)

rez_set_archive(
	url_tools pyside/Tools-${tools_version}.tar.gz
    https://github.com/pyside/Tools/releases/tag/${tools_version}
)

rez_set_archive(
	url_shiboken pyside/Shiboken-${shiboken_version}.tar.gz
    https://github.com/pyside/Shiboken/releases/tag/${shiboken_version}
)


add_custom_target(
    build_pyside
    ALL
    COMMAND bash ./build.sh ${CMAKE_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} $ENV{REZ_REPO_PAYLOAD_DIR} ${pyside_version} ${shiboken_version} ${tools_version}
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    VERBATIM
)

install(
    CODE
    "execute_process(
        COMMAND make install
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/objdir
    )"
)
