# Cookiecutter template for CatalystNeuro projects
This repo serves as a generic template generator for all conversion projects undertaken by the CatalystNeuro team. 
The project is based and shares the structure of our
[generic template](https://github.com/catalystneuro/my-lab-to-nwb-template) and extends it further by means of
[cookiecutter](https://github.com/cookiecutter/cookiecutter) to auto-generate the rest of the configuration.

# How to use it

## 1) Install `cookiecutter`:

Install the latest cookiecutter version if you haven't installed it yet:

    pip install -U cookiecutter

## 2) Run `cookiecutter` with this repo and answer some prompts

Then, use the following `cookiecutter` command to generate a `CatalystNeuro` conversion project structure:

    cookiecutter https://github.com/catalystneuro/cookiecutter-my-lab-to-nwb-template

This will ask some questions that determine the project structure as in the following example:

    lab [Lab Name]: Tank
    repo_name [tank-lab-to-nwb]: 
    conversion_name [embargo2002a]: towers_task

Where the `lab` usually corresponds to the principal investigator name, `repo_name` is the name of the github 
repositry and `conversion_name` is the name of the specific conversion to be carried out. 

Leave the prompt unanswered (blank) to accept the default suggestion in square brackets (e.g. `repo name` will be 
assigned the value of `tank-lab-to-nwb` as the space is left blank). We suggest to use the name of the author plus the 
year for the conversion name.

For conversions concerning data under embargo we suggest a name following the pattern described in the brackets (i.e.
`embargo22a`). The general form is `embargo{year}{letter}` where year is the year of the conversion and letter can 
be a, b, c, etc. in case there is more than one conversion that year.

## 3) Copy the generated content to a repo as you need it

After the questions in the prompt are answered as above, `cookiecutter` generates a directory with the following 
structure:

    tank-lab-to-nwb/
    ├── LICENSE
    ├── make_env.yml
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── src
        ├── tank_lab_to_nwb
        │   └── towers_task
        │       ├── behaviorinterface.py
        │       ├── convert_session.py
        │       ├── metadata.yml
        │       ├── nwbconverter.py
        │       ├── requirements.txt
        │       └── __init__.py
        └── __init__.py


You can then modify this to suit the particular needs of the ongoing conversion.

The last step is to create an empty repo with the same name as the generated directory from our team 
[github account](https://github.com/catalystneuro) and just fill the contents with the ones in the directory 
generated by `cookiecuter`.

## 4) Configure the repo

### Pre-commit
For new repos, an extra step of allowing the black auto-commit CI bot may have to be enabled at: https://results.
pre-commit.ci/

To enable the pre-commit hook locally use the two following steps:
```
pip install pre-commit
pre-commit install
```

The `.pre-commit-config.yaml` is already included in the repository.
