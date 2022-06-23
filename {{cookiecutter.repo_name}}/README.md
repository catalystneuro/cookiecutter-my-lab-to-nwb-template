# {{cookiecutter.repo_name}}
NWB conversion scripts for {{cookiecutter.lab}} lab data to the [neuro data without borders](https://www.nwb.org/) data format.

# Clone and dev install
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

To run a specific conversion first install the dependecy specific requirements:
```
pip install -r src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_requirements.txt 
```

And then run the conversion
```
python src/{{cookiecutter.repo_name_slug}}/{{cookiecutter.conversion_name}}/{{cookiecutter.conversion_name}}_conversion_script.py
```
Where conversion_name is for example {{cookiecutter.conversion_name}}.



# Repo structure
Each conversion is organized in a directory of its own in the `src` directory. For example, for the conversion `{{cookiecutter.conversion_name}}` you can find a directory located in `src/{{cookiecutter.repo_name}}/{{cookiecutter.conversion_name}}`. Inside of this directory, you can find the following files:

* `{{cookiecutter.conversion_name}}_convert_script.py`: this is the script that you must run in order to run the conversion pipeline.
* `{{cookiecutter.conversion_name}}_requirements.txt`: dependencies specific to this conversion repo_name.
* `{{cookiecutter.conversion_name}}_metadata.yml`: metadata in yaml format for this specific conversion.
* `{{cookiecutter.conversion_name}}behaviorinterface.py`: the behavior interface. Usually ad-hoc for each conversion.
* `{{cookiecutter.conversion_name}}nwbconverter.py`: The place where the `NWBConverter` class is defined.
