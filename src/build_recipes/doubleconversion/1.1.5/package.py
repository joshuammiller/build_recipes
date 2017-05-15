name = "doubleconversion"

version = "1.1.5"

authors = [
    "doubleconversion"
]

description = \
    """
    Google's library for efficient floating point conversion
    """

build_requires = [
    "gcc-4.8.3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "4bbc480e-c10b-44c7-845e-6170c129041d"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
