# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "requirements.txt")) as f:
    install_requires = f.read().strip().split("\n")

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="{{cookiecutter.repo_name}}",
    version="0.0.1",
    description="NWB conversion scripts, functions, and classes for an arbitrary conversion repo_name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="CatalystNeuro",
    email="ben.dichter@catalystneuro.com",
    url = "https://github.com/catalystneuro/{{cookiecutter.repo_name}}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=install_requires,
)
