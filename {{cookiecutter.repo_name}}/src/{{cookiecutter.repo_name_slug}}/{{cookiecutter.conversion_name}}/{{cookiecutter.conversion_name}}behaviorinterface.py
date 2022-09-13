"""Primary class defining conversion of experiment-specific behavior."""
from pynwb.file import NWBFile

from neuroconv.basedatainterface import BaseDataInterface

class {{cookiecutter.conversion_name_camel_case}}BehaviorInterface(BaseDataInterface):
    """My behavior interface docstring"""

    def __init__(self):
        # Point to data
        pass

    def get_metadata(self):
        # Automatically retrieve as much metadata as possible
        
        return dict()

    def run_conversion(self, nwbfile: NWBFile, metadata: dict):
        # All the custom code to write through PyNWB
        
        return nwbfile
