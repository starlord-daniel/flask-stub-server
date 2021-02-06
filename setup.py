import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="flask-stub-server",
    version="0.0.1",
    author="Daniel Heinze",
    author_email="daniel.heinze@microsoft.com",
    description=("Provides the user with a Docker container, "
                 "that exposes endpoints, which can be configured via json file."),
    license="MIT",
    keywords="python stub server flask",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Pre-Alpha",
        "Topic :: Server",
        "License :: OSI Approved :: MIT",
    ]
)
