from __future__ import print_function, with_statement
from setuptools import setup, find_packages


setup(
    name="rez_{{cookiecutter.extension_command}}",
    version="{{cookiecutter.extension_version}}",
    package_dir={
        "rez_{{cookiecutter.extension_command}}": "rez_{{cookiecutter.extension_command}}"
    },
    packages=find_packages(where="."),
)
