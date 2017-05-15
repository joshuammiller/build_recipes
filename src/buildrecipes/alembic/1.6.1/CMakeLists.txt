CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(alembic_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_alembic alembic/alembic-${alembic_version}.tar.gz
    https://github.com/alembic/alembic/archive/${alembic_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    alembic
    URL ${url_alembic}
    PREFIX alembic
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} <SOURCE_DIR>
                                        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
                                        -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
                                        -DOPENEXR_ROOT=$ENV{REZ_OPENEXR_ROOT}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
)
