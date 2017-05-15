name = "qt"

version = "4.8.7"

authors = [
    "Qt"
]

description = \
    """
    Cross-platform open source UI framework for C++
    """

build_requires = [
    "gcc-4.8.3"
]

tools = [
    "assistant",
    "designer",
    "lconvert",
    "linguist",
    "lrelease",
    "lupdate"
    "moc",
    "qmake",
    "qtconfig"
    "rcc",
    "uic",
    "uic3"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "56f07d0f-13ff-4ded-92b5-72c392dee94e"


def commands():
    env.PATH.append("{root}/bin")

    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.QT4DIR = "{root}"
    env.QTDIR = env.QT4DIR

    env.QT4BINDIR = "{root}/bin"
    env.QTBINDIR = env.QT4BINDIR

    env.QT4LIBDIR = "{root}/lib:{root}/lib64"
    env.QTLIBDIR = env.QT4LIBDIR

    env.QT4INCDIR = "{root}/include"
    env.QTINCDIR = env.QT4INCDIR

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

