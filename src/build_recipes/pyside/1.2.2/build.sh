#!/usr/bin/bash

build_dir=$1
install_dir=$2
archive_dir=$3
pyside_ver=$4
shiboken_ver=$5
tools_ver=$6

cd ${build_dir}

alldirs=("shiboken" "pyside" "pyside-tools")

if [ ! -d pyside ]; then
    mkdir pyside
    archive=${archive_dir}/pyside/PySide-${pyside_ver}.tar.gz
    echo "Extracting pyside from ${archive}..."
    tar xvf ${archive} -C pyside --strip-components=1
fi

if [ ! -d pyside-tools ]; then
    mkdir pyside-tools
    archive=${archive_dir}/pyside/Tools-${tools_ver}.tar.gz
    echo "Extracting pyside-tools from ${archive}..."
    tar xvf ${archive} -C pyside-tools --strip-components=1
fi

if [ ! -d shiboken ]; then
    mkdir shiboken
    archive=${archive_dir}/pyside/Shiboken-${shiboken_ver}.tar.gz
    echo "Extracting shiboken from ${archive}..."
    tar xvf ${archive} -C shiboken --strip-components=1
fi

for d in "${alldirs[@]}" ; do
    rm -rf "$d/build"
    mkdir -p "$d/build"
    (
        cd "$d/build"
        cmake .. -DCMAKE_INSTALL_PREFIX=${install_dir} \
                 -DENABLE_ICECC=0 \
                 -DENABLE_GCC_OPTIMIZATION=On \
                 && make -j${REZ_BUILD_THREAD_COUNT} && make install || exit 1
    ) || exit 1

done