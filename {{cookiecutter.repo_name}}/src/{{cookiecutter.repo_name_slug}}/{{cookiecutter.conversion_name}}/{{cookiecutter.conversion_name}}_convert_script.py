"""Primary script to run to convert an entire session of data using the NWBConverter."""
from nwb_conversion_tools.utils import load_dict_from_file, dict_deep_update

from {{cookiecutter.repo_name_slug}}.{{cookiecutter.conversion_name}} import {{cookiecutter.conversion_name_camel_case}}NWBConverter
from pathlib import Path

example_path = Path("D:/ExampleNWBConversion")
example_session_id = example_path.stem
nwbfile_path = example_path / f"{example_session_id}.nwb"

metadata_path = Path(__file__) / "{{cookiecutter.conversion_name}}_metadata.yaml"

source_data = dict(
    Recording=dict(),
    LFP=dict(),
    Sorting=dict(),
    Behavior=dict(),
)

converter = {{cookiecutter.conversion_name_camel_case}}NWBConverter(source_data=source_data)

metadata = converter.get_metadata()
metadata_from_yaml = load_dict_from_file(metadata_path)
metadata = dict_deep_update(metadata, metadata_from_yaml)

converter.run_conversion(metadata=metadata, nwbfile_path=nwbfile_path)
