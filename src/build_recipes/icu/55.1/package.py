name = "icu"

version = "55.1"

authors = [
    "GNU"
]

description = \
    """
    GNU Internationl Components for Unicode.
    """

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

build_requires = [
    "gcc-4.8"
]

uuid = "b1f78de1-0a48-493b-9469-4914be2ce998"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CC = "gcc"
        env.CXX = "g++"
