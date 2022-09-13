"""Primary script to run to convert an entire session of data using the NWBConverter."""
from pathlib import Path

from neuroconv.utils import load_dict_from_file, dict_deep_update

from {{cookiecutter.repo_name_slug}}.{{cookiecutter.conversion_name}} import {{cookiecutter.conversion_name_camel_case}}NWBConverter

example_path = Path("D:/ExampleNWBConversion")
example_session_id = example_path.stem
nwbfile_path = example_path / f"{example_session_id}.nwb"

source_data = dict()

# Add Recording
source_data.update(dict(Recording=dict()))

# Add LFP
source_data.update(dict(LFP=dict()))

# Add Sorting
source_data.update(dict(Sorting=dict()))

# Add Behavior
source_data.update(dict(Behavior=dict()))

converter = {{cookiecutter.conversion_name_camel_case}}NWBConverter(source_data=source_data)

# Update default metadata with the one in the editable yaml file in this directory
editable_metadata_path = Path(__file__).parent / "{{cookiecutter.conversion_name}}_metadata.yaml"
editable_metadata = load_dict_from_file(editable_metadata_path)
metadata = converter.get_metadata()
metadata = dict_deep_update(metadata, editable_metadata)

converter.run_conversion(metadata=metadata, nwbfile_path=nwbfile_path)
