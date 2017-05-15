name = "alembic"

version = "1.6.1"

authors = [
    "alembic"
]

description = \
    """
    Open source standard for storing 3d geometry
    """

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

requires = [
    "openexr-2.2"
]

build_requires = [
    "gcc-4.8.3",
    "openexr-2.2"
]

tools = [
    "abcdiff",
    "abcecho",
    "abcechobounds",
    "abcls",
    "abcstitcher",
    "abctree"
]

uuid = "9e112354-c345-4338-8271-077a69cc9f7a"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
