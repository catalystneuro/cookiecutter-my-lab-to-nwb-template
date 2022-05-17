"""Primary NWBConverter class for this dataset."""
from nwb_conversion_tools import (
    NWBConverter,
    SpikeGLXRecordingInterface,
    SpikeGLXLFPInterface,
    PhySortingInterface,
)

from my_lab_to_nwb.my_ecephys_dataset import MyEcephysBehaviorInterface


class MyEcephysDatasetNWBConverter(NWBConverter):
    """Primary conversion class for my extracellular electrophysiology dataset."""

    data_interface_classes = dict(
        Recording=SpikeGLXRecordingInterface,
        LFP=SpikeGLXLFPInterface,
        Sorting=PhySortingInterface,
        Behavior=MyEcephysBehaviorInterface,
    )
