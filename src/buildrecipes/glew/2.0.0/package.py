name = "glew"

version = "2.0.0"

authors = [
    "glew"
]

description = \
    """
    ILM's high dynamic-range (HDR) image file format library.
    """

build_requires = [
    "gcc-4.8.3",
    "tbb"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "211df4bf-e825-4ec6-966c-ea64fb4e9bd5"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
