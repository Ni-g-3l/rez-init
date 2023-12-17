from __future__ import print_function, with_statement
from setuptools import setup, find_packages


setup(
    name="rez_init",
    version="0.1.0",
    package_dir={"rez_init": "rez_init"},
    install_requires=["cookiecutter"],
    packages=find_packages(where="."),
)
