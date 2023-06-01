# {{cookiecutter.repo_name}}
NWB conversion scripts for {{cookiecutter.lab}} lab data to the [Neurodata Without Borders](https://nwb-overview.readthedocs.io/) data format.


## Installation
## Basic installation

You can install the latest release of the package with pip:

```
pip install {{cookiecutter.repo_name}}
```

We recommend that you install the package inside a [virtual environment](https://docs.python.org/3/tutorial/venv.html). A simple way of doing this is to use a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) from the `conda` package manager ([installation instructions](https://docs.conda.io/en/latest/miniconda.html)). Detailed instructions on how to use conda environments can be found in their [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Running a specific conversion
Once you have installed the package with pip, you can run any of the conversion scripts in a notebook or a python file:

https://github.com/catalystneuro/{{cookiecutter.repo_name}}//tree/main/src/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_conversion_script.py




## Installation from Github
Another option is to install the package directly from Github. This option has the advantage that the source code can be modifed if you need to amend some of the code we originally provided to adapt to future experimental differences. To install the conversion from GitHub you will need to use `git` ([installation instructions](https://github.com/git-guides/install-git)). We also recommend the installation of `conda` ([installation instructions](https://docs.conda.io/en/latest/miniconda.html)) as it contains all the required machinery in a single and simple instal

From a terminal (note that conda should install one in your system) you can do the following:

```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
conda env create --file make_env.yml
conda activate {{cookiecutter.repo_name}}-env
```

This creates a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) which isolates the conversion code from your system libraries.  We recommend that you run all your conversion related tasks and analysis from the created environment in order to minimize issues related to package dependencies.

Alternatively, if you want to avoid conda altogether (for example if you use another virtual environment tool) you can install the repository with the following commands using only pip:

```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
pip install -e .
```

Note:
both of the methods above install the repository in [editable mode](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs).

### Running a specific conversion
To run a specific conversion, you might need to install first some conversion specific dependencies that are located in each conversion directory:
```
pip install -r src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_requirements.txt
```

You can run a specific conversion with the following command:
```
python src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_conversion_script.py
```

## Repository structure
Each conversion is organized in a directory of its own in the `src` directory:

    {{cookiecutter.repo_name}}/
    ├── LICENSE
    ├── make_env.yml
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── src
        ├── {{cookiecutter.repo_name_slug}}
        │   ├── conversion_directory_1
        │   └── {{cookiecutter.conversion_name}}
        │       ├── {{cookiecutter.conversion_name}}behaviorinterface.py
        │       ├── {{cookiecutter.conversion_name}}_convert_session.py
        │       ├── {{cookiecutter.conversion_name}}_metadata.yml
        │       ├── {{cookiecutter.conversion_name}}nwbconverter.py
        │       ├── {{cookiecutter.conversion_name}}_requirements.txt
        │       ├── {{cookiecutter.conversion_name}}_notes.md

        │       └── __init__.py
        │   ├── conversion_directory_b

        └── __init__.py

 For example, for the conversion `{{cookiecutter.conversion_name}}` you can find a directory located in `src/{{cookiecutter.repo_name}}/{{cookiecutter.conversion_name}}`. Inside each conversion directory you can find the following files:

* `{{cookiecutter.conversion_name}}_convert_sesion.py`: this script defines the function to convert one full session of the conversion.
* `{{cookiecutter.conversion_name}}_requirements.txt`: dependencies specific to this conversion.
* `{{cookiecutter.conversion_name}}_metadata.yml`: metadata in yaml format for this specific conversion.
* `{{cookiecutter.conversion_name}}behaviorinterface.py`: the behavior interface. Usually ad-hoc for each conversion.
* `{{cookiecutter.conversion_name}}nwbconverter.py`: the place where the `NWBConverter` class is defined.
* `{{cookiecutter.conversion_name}}_notes.md`: notes and comments concerning this specific conversion.

The directory might contain other files that are necessary for the conversion but those are the central ones.
