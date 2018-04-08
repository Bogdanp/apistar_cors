import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("apistar_cors.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


setup(
    name="apistar_cors",
    version=version,
    description="CORS support for API Star.",
    long_description="Visit https://github.com/Bogdanp/apistar_cors for more information.",
    packages=[],
    py_modules=["apistar_cors"],
    install_requires=[
        "apistar>=0.4,<0.5",
        "wsgicors>=0.7,<0.8",
    ],
    python_requires=">=3.5",
    include_package_data=True,
)
