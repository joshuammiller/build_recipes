name = "pyside"

version = "1.2.2"

authors = [
    "Qt"
]

description = \
    """
    Python bindings for Qt
    """

build_requires = [
    "gcc-4.8.3",
    "qt-4.8",
    "python-2.7",
    "icu-55"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "fe3d87a0-e2fb-4f81-afbc-977ac1492234"


def commands():
    env.PYSIDESANDBOXPATH = "{root}"

    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    python_path = "{root}/lib/python2.7/site-packages"

    env.PYTHONPATH.prepend(python_path)
