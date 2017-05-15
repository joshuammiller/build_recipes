name = "tbb"

version = "4.3"

authors = [
    "Intel"
]

description = \
    """
    Intel Threading Building Blocks.
    """

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "d1ed9aca-09bb-4e3d-8db0-c42faf4c0231"


def commands():
    env.PATH.append("{root}/include")
    env.LD_LIBRARY_PATH.append("{root}/lib/release")

    if building:
        env.TBB_INCLUDE_DIR = "{root}/include"
