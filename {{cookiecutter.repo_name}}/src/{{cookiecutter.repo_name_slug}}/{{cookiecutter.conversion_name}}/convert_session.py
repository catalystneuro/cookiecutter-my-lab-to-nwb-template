"""Primary script to run to convert an entire session for of data using the NWBConverter."""
from pathlib import Path
from typing import Union
import datetime
from zoneinfo import ZoneInfo

from neuroconv.utils import load_dict_from_file, dict_deep_update

from .{{cookiecutter.conversion_name}} import {{cookiecutter.conversion_name_camel_case}}NWBConverter


def session_to_nwb(data_dir_path: Union[str, Path], output_dir_path: Union[str, Path], stub_test: bool = False):

    data_dir_path = Path(data_dir_path)
    output_dir_path = Path(output_dir_path)
    if stub_test:
        output_dir_path = output_dir_path / "nwb_stub"
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    session_id = "subject_identifier_usually"
    nwbfile_path = output_dir_path / f"{session_id}.nwb"

    source_data = dict()
    conversion_options = dict()

    # Add Recording
    source_data.update(dict(Recording=dict()))
    conversion_options.update(dict(Recording=dict()))
    
    # Add LFP
    source_data.update(dict(LFP=dict()))
    conversion_options.update(dict(LFP=dict()))

    # Add Sorting
    source_data.update(dict(Sorting=dict()))
    conversion_options.update(dict(Sorting=dict()))

    # Add Behavior
    source_data.update(dict(Behavior=dict()))
    conversion_options.update(dict(Behavior=dict()))

    converter = {{cookiecutter.conversion_name_camel_case}}NWBConverter(source_data=source_data)
    
    # Add datetime to conversion
    metadata = converter.get_metadata()
    date = datetime.datetime(year=2020, month=1, day=1, tzinfo=ZoneInfo("US/Eastern"))
    metadata["NWBFile"]["session_start_time"] = date
    
    # Update default metadata with the editable in the corresponding yaml file
    editable_metadata_path = Path(__file__).parent / "{{cookiecutter.conversion_name}}_metadata.yaml"
    editable_metadata = load_dict_from_file(editable_metadata_path)
    metadata = dict_deep_update(metadata, editable_metadata)

    # Run conversion
    converter.run_conversion(metadata=metadata, nwbfile_path=nwbfile_path, conversion_options=conversion_options)


if __name__ == "__main__":
    
    # Parameters for conversion
    data_dir_path = Path("/Directory/With/Raw/Formats/")
    output_dir_path = Path("~/conversion_nwb/")
    stub_test = False

    session_to_nwb(data_dir_path=data_dir_path, output_dir_path=output_dir_path, stub_test=stub_test)