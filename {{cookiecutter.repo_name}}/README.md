# {{cookiecutter.repo_name}}
NWB conversion scripts for {{cookiecutter.lab}} lab data to the
[Neurodata Without Borders](https://nwb-overview.readthedocs.io/) data format.


## Installation
## Basic installation

You can install the latest release of the package with pip:

```
pip install {{cookiecutter.repo_name}}
```

We recommend that you install the package inside a [virtual environment](https://docs.python.org/3/tutorial/venv.
html). A simple way of doing this is to use a [conda environment](https://docs.conda.
io/projects/conda/en/latest/user-guide/concepts/environments.html) from the `conda` package manager ([installation 
instructions](https://docs.conda.io/en/latest/miniconda.html)). Detailed instructions on how to use conda 
environments can be found in their [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Running a specific conversion
Once you have installed the package with pip, you can run any of the conversion scripts in a notebook or a python file:

https://github.com/catalystneuro/{{cookiecutter.repo_name}}//tree/main/src/{{cookiecutter.conversion_name}}/convert_session.py

Copy or download this file run the script with the following command:

```
python convert_session.py
```

## Installation from GitHub
Another option is to install the package directly from GitHub. This option has the advantage that the source code 
can be modified if you need to amend some of the code we originally provided to adapt to future experimental 
differences. To install the conversion from GitHub you will need to use `git` ([installation instructions] (https://github.com/git-guides/install-git)). 
We also recommend the installation of `conda` ([installation instructions](https://docs.conda.io/en/latest/miniconda.html)) as it contains all the required 
machinery in a single and simple install.

From a terminal (note that conda should install one in your system) you can do the following:

```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
conda env create --file make_env.yml
conda activate {{cookiecutter.repo_name}}-env
```

This creates a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) which isolates the conversion code from your system libraries.  We recommend that you run all your conversion related tasks and analysis from the created environment in order to minimize issues related to package dependencies.

Alternatively, if you want to avoid conda altogether (for example if you use another virtual environment tool) you 
can install the repository with the following commands using only pip:

```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
pip install --editable .
```

Note:
both of the methods above install the repository in [editable mode](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs).

### Running a specific conversion
If the project has more than one conversion, you can install the requirements for a specific conversion with the following command:
```
pip install --editable .[{{cookiecutter.conversion_name}}]
```

You can run a specific conversion with the following command:
```
python src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/convert_session.py
```

## Helpful Definitions

This conversion project is comprised primarily by DataInterfaces, NWBConverters, and conversion scripts.

In neuroconv, a [DataInterface](https://neuroconv.readthedocs.io/en/main/user_guide/datainterfaces.html) is a class that specifies the procedure to convert a single data modality to NWB.
This is usually accomplished with a single read operation from a distinct set of files.
For example, in this conversion, the `{{cookiecutter.conversion_name_camel_case}}BehaviorInterface` contains the code that converts all of the behavioral data to NWB from raw <FILE_TYPE> files.

In neuroconv, a [NWBConverter](https://neuroconv.readthedocs.io/en/main/user_guide/nwbconverter.html) is a class that combines many data interfaces and specifies the relationships between them, such as temporal alignment.
This allows users to combine multiple modalities into a single NWB file in an efficient and modular way.

In this conversion project, the conversion scripts determine which sessions to convert,
instantiate the appropriate NWBConverter object,
and convert all of the specified sessions, saving them to an output directory of .nwb files.


## Repository structure
Each conversion is organized in a directory of its own in the `src` directory:

    {{cookiecutter.repo_name}}/
    ├── LICENSE
    ├── make_env.yml
    ├── pyproject.toml
    ├── README.md
    └── src
        ├── {{cookiecutter.repo_name_slug}}
        │   └── {{cookiecutter.conversion_name}}
        │       ├── conversion_notes.md
        │       ├── behaviorinterface.py
        │       ├── convert_session.py
        │       ├── metadata.yml
        │       ├── nwbconverter.py
        │       └── __init__.py
        │   ├── conversion_directory_b

        └── __init__.py

For example, for the conversion `{{cookiecutter.conversion_name}}` you can find a directory located in `src/{{cookiecutter.repo_name}}/{{cookiecutter.conversion_name}}`. 
Inside each conversion directory you can find the following files:


* `convert_sesion.py`: this script defines the function to convert one full session of the conversion. 
* `metadata.yml`: metadata in yaml format for this specific conversion.
* `behaviorinterface.py`: the behavior interface. Usually ad-hoc for each conversion.
* `nwbconverter.py`: the place where the `NWBConverter` class is defined.
* `conversion_notes.md`: notes and comments concerning this specific conversion.

The directory might contain other files that are necessary for the conversion but those are the central ones.
