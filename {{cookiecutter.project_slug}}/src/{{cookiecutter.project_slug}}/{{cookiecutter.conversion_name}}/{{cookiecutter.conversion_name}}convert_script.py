"""Primary script to run to convert an entire session of data using the NWBConverter."""
from nwb_conversion_tools.utils import load_dict_from_file, dict_deep_update

from my_lab_to_nwb.my_ecephys_dataset import MyEcephysDatasetNWBConverter
from pathlib import Path

example_path = Path("D:/ExampleNWBConversion")
example_session_id = example_path.stem
nwbfile_path = example_path / f"{example_session_id}.nwb"

metadata_path = Path(__file__) / "ecephys_dataset_metadata.yaml"
metadata_from_yaml = load_dict_from_file(metadata_path)

source_data = dict(
    Recording=dict(),
    LFP=dict(),
    Sorting=dict(),
    Behavior=dict(),
)

my_ecephys_dataset_converter = MyEcephysDatasetNWBConverter(source_data=source_data)

metadata = example_converter.get_metadata()
metadata = dict_deep_update(metadata, metadata_from_yaml)

example_converter.run_conversion(metadata=metadata, nwbfile_path=nwbfile_path)
