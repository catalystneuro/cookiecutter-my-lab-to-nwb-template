# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup, find_packages

requirements_file_path = Path(__file__).parent / "requirements.txt"
with open(requirements_file_path) as file:
    install_requires = file.readlines()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="{{cookiecutter.repo_name}}",
    version="0.0.1",
    description="NWB conversion scripts, functions, and classes for {{cookiecutter.lab}} conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="CatalystNeuro",
    author_email="ben.dichter@catalystneuro.com",
    url = "https://github.com/catalystneuro/{{cookiecutter.repo_name}}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=install_requires,
)
