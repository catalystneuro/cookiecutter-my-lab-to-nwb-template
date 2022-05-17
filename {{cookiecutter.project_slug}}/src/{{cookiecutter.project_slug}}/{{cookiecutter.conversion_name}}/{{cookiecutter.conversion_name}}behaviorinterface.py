"""Primary class defining conversion of experiment-specific behavior."""
from nwb_conversion_tools import BaseDataInterface


class MyEcephysBehaviorInterface(BaseRecordingExtractorInterface):
    """My behavior interface specific to the ecephys experiments."""

    def __init__(self):
        # Point to data
        pass

    def get_metadata(self):
        # Automatically retrieve as much metadata as possible
        pass

    def run_conversion(self):
        # All the custom code to write through PyNWB
        pass
