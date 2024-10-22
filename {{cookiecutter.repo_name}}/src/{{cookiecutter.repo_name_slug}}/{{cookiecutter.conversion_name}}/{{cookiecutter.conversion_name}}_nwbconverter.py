"""Primary NWBConverter class for this dataset."""
from neuroconv import NWBConverter
from neuroconv.datainterfaces import (
    SpikeGLXRecordingInterface,
    PhySortingInterface,
)

from .{{cookiecutter.conversion_name}} import {{cookiecutter.conversion_name_camel_case}}BehaviorInterface


class {{cookiecutter.conversion_name_camel_case}}NWBConverter(NWBConverter):
    """Primary conversion class for my extracellular electrophysiology dataset."""

    data_interface_classes = dict(
        Recording=SpikeGLXRecordingInterface,
        Sorting=PhySortingInterface,
        Behavior={{cookiecutter.conversion_name_camel_case}}BehaviorInterface,
    )
