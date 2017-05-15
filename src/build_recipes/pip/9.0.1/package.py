name = 'pip'

version = '9.0.1'

tools = [
    'pip',
]

# variants = [
#     ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04", "python-2.7"]
# ]

build_requires = [
    'setuptools-33.0'
]

requires = [
    'setuptools-33.0'
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.pip'
