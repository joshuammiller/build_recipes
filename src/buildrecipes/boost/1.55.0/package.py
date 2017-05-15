name = "boost"

version = "1.55.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04", "python-2.7"]
]

uuid = "f8b08e3c-2b3f-4121-b60c-0b26224cb00d"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.BOOST_INCLUDE_DIR = "{root}/include"
