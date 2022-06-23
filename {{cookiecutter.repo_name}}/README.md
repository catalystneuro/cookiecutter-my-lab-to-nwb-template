# {{cookiecutter.repo_name}}
NWB conversion scripts for {{cookiecutter.lab}} lab data to the [neuro data without borders](https://www.nwb.org/) data format.

## Clone and dev install
To run the following repo you need to have installed both git and pip then do the following.

```
$ git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
$ pip install -e .
```

Alternatively, to clone the repository and set up a conda environment, do:
```
$ git clone https://github.com/catalystneuro/{{cookiecutter.repo_name}}
$ cd nwb-conversion-tools
$ conda env create --file make_env.yml
$ conda activate {{cookiecutter.repo_name}}-env
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
        │   └── {{cookiecutter.conversion_name}}`
        │       ├── {{cookiecutter.conversion_name}}behaviorinterface.py
        │       ├── {{cookiecutter.conversion_name}}_convert_script.py
        │       ├── {{cookiecutter.conversion_name}}_metadata.yml
        │       ├── {{cookiecutter.conversion_name}}nwbconverter.py
        │       ├── {{cookiecutter.conversion_name}}_requirements.txt
        │       └── __init__.py
        │   ├── conversion_directory_b

        └── __init__.py

 For example, for the conversion `{{cookiecutter.conversion_name}}` you can find a directory located in `src/{{cookiecutter.repo_name}}/{{cookiecutter.conversion_name}}`. Inside each conversion directory you can find the following files:

* `{{cookiecutter.conversion_name}}_convert_script.py`: this is the cemtral script that you must run in order to perform the full conversion.
* `{{cookiecutter.conversion_name}}_requirements.txt`: dependencies specific to this conversion specifically.
* `{{cookiecutter.conversion_name}}_metadata.yml`: metadata in yaml format for this specific conversion.
* `{{cookiecutter.conversion_name}}behaviorinterface.py`: the behavior interface. Usually ad-hoc for each conversion.
* `{{cookiecutter.conversion_name}}nwbconverter.py`: The place where the `NWBConverter` class is defined.

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
