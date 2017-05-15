name = "opensubdiv"

version = "3.0.5"

authors = [
    "opensubdiv"
]

description = \
    """
    Pixar's Open Source Library for Subdivision Surfaces
    """

build_requires = [
    "gcc-4.8.2",
    "tbb-4.3+<5.0",
    "glfw-3.0.4+<4.0",
    "glew-2.0+<3.0"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "85a041fe-048f-48eb-ac5b-d6e19210976e"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
