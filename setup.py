import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


# https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme
MAJOR = "0"  # version when they make incompatible API changes
MINOR = "1"  # version when they add functionality in a backwards-compatible manner
MAINTENANCE = "5"  # version when they make backwards-compatible bug fixes.
RELEASE_TYPE = "a1"

setup(
    name="flask-stub-server",
    version=f"{MAJOR}.{MINOR}.{MAINTENANCE}{RELEASE_TYPE}",
    author="Daniel Heinze",
    author_email="daniel.heinze@microsoft.com",
    description=("This package provides the user with an easy to use endpoint generator, "
                 "which that exposes endpoints that are defined through a config JSON file. "
                 "Additionally, data files can be added and linked to return richer data."),
    license="MIT",
    url="https://github.com/starlord-daniel/flask-stub-server",
    keywords="python stub server flask",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["flask_stub_server", "flask_stub_server/endpoint_gen"],
    python_requires='>=3.9',
    install_requires=['Flask>=1.1.2'],
)
