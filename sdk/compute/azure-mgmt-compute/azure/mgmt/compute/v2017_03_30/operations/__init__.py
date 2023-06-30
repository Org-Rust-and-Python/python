# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import AvailabilitySetsOperations
from ._operations import VirtualMachineExtensionImagesOperations
from ._operations import VirtualMachineExtensionsOperations
from ._operations import VirtualMachinesOperations
from ._operations import VirtualMachineImagesOperations
from ._operations import UsageOperations
from ._operations import VirtualMachineSizesOperations
from ._operations import ImagesOperations
from ._operations import ResourceSkusOperations
from ._operations import VirtualMachineScaleSetsOperations
from ._operations import VirtualMachineScaleSetExtensionsOperations
from ._operations import VirtualMachineScaleSetRollingUpgradesOperations
from ._operations import VirtualMachineScaleSetVMsOperations
from ._operations import DisksOperations
from ._operations import SnapshotsOperations
from ._operations import VirtualMachineRunCommandsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AvailabilitySetsOperations",
    "VirtualMachineExtensionImagesOperations",
    "VirtualMachineExtensionsOperations",
    "VirtualMachinesOperations",
    "VirtualMachineImagesOperations",
    "UsageOperations",
    "VirtualMachineSizesOperations",
    "ImagesOperations",
    "ResourceSkusOperations",
    "VirtualMachineScaleSetsOperations",
    "VirtualMachineScaleSetExtensionsOperations",
    "VirtualMachineScaleSetRollingUpgradesOperations",
    "VirtualMachineScaleSetVMsOperations",
    "DisksOperations",
    "SnapshotsOperations",
    "VirtualMachineRunCommandsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
