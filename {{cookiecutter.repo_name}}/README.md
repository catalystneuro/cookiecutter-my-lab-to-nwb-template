# {{cookiecutter.repo_name}}
NWB conversion scripts for {{cookiecutter.lab}} lab data to the [neuro data without borders](https://nwb-overview.readthedocs.io/) data format.

## Clone and install
To run the conversion some basic machinery is needed: **python, git and pip**. For most users, we recommend you to install `conda` ([installation instructions](https://docs.conda.io/en/latest/miniconda.html)) as it contains all the required machinery in a single and simple install. If your system is windows you might also need to install `git` ([installation instructions](https://github.com/git-guides/install-git)) to interact with this repository.

From a terminal (note that conda should install one in your system) you can do the following:

```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
conda env create --file make_env.yml
conda activate {{cookiecutter.repo_name}}-env
```
This create a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) which isolates the conversion from your system. We recommend that you run all your conversion related tasks and analysis from that environment to minimize the intereference of this code with your own system.

Alternatively, if you want to avoid conda altogether (for example if you use another virtual environment tool) you can install the repository with the following commands using only pip:
```
git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
pip install -e .
```

Note:
both of the methods above install the repository in [editable mode](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs) 

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
        │   └── {{cookiecutter.conversion_name}}`
        │       ├── {{cookiecutter.conversion_name}}behaviorinterface.py
        │       ├── {{cookiecutter.conversion_name}}_convert_script.py
        │       ├── {{cookiecutter.conversion_name}}_metadata.yml
        │       ├── {{cookiecutter.conversion_name}}nwbconverter.py
        │       ├── {{cookiecutter.conversion_name}}_requirements.txt
        │       ├── {{cookiecutter.conversion_name}}_notes.md

        │       └── __init__.py
        │   ├── conversion_directory_b

        └── __init__.py

 For example, for the conversion `{{cookiecutter.conversion_name}}` you can find a directory located in `src/{{cookiecutter.repo_name}}/{{cookiecutter.conversion_name}}`. Inside each conversion directory you can find the following files:

* `{{cookiecutter.conversion_name}}_convert_script.py`: this is the cemtral script that you must run in order to perform the full conversion.
* `{{cookiecutter.conversion_name}}_requirements.txt`: dependencies specific to this conversion specifically.
* `{{cookiecutter.conversion_name}}_metadata.yml`: metadata in yaml format for this specific conversion.
* `{{cookiecutter.conversion_name}}behaviorinterface.py`: the behavior interface. Usually ad-hoc for each conversion.
* `{{cookiecutter.conversion_name}}nwbconverter.py`: the place where the `NWBConverter` class is defined.
* `{{cookiecutter.conversion_name}}_notes.md`: notes and comments concerning this specific conversion.

The directory might contain other files that are necessary for the conversion but those are the central ones.

## Running a specific conversion
To run a specific conversion, you might need to install first some conversion specific dependencies that are located in each conversion directory:
```
pip install -r src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_requirements.txt 
```

You can run a specific conversion with the following command:
```
python src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_conversion_script.py
```
