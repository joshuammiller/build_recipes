name = "glfw"

version = "3.0.4"

authors = [
    "glfw"
]

description = \
    """
    ILM's high dynamic-range (HDR) image file format library.
    """

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "2f35e65c-07a8-4a01-9de5-7bf705f8f960"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
