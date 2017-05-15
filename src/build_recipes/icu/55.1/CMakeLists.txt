CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# set(icu_major_version $ENV{REZ_BUILD_PROJECT_MAJOR_VERSION})
# set(icu_minor_version $ENV{REZ_BUILD_PROJECT_MINOR_VERSION})

set(icu_major_version 55)
set(icu_minor_version 1)

rez_set_archive(
	url_icu icu/icu4c-${icu_major_version}_${icu_minor_version}-src.tgz
	http://download.icu-project.org/files/icu4c/${icu_major_version}_${icu_minor_version}/icu4c-${icu_major_version}_${icu_minor_version}-src.tgz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    icu
    URL ${url_icu}
    PREFIX icu
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND <SOURCE_DIR>/source/configure -prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
