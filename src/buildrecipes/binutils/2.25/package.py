name = "binutils"

version = "55.1"

authors = [
    "GNU"
]

description = \
    """
    GNU project C and C++ compiler.
    """

# variants = [
#     ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
# ]

tools = [
    "add2line",
    "ar",
    "ld",
    "nm",
    "as",
    "objcopy",
    "objdump",
    "size",
    "strings",
    "strip",
    "elfedit",
    "gprof"
]

uuid = "repository.binutils"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    # if building:
    #     env.CC = "{root}/bin/gcc"
    #     env.CXX = "{root}/bin/g++"
