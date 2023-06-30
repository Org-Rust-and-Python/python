# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Code(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation status code."""

    SUCCEEDED = "Succeeded"
    """Extension was created/updated successfully."""
    FAILED = "Failed"
    """Extension was not created/updated successfully. See operation status message for more details."""


class IsEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the extension is enabled."""

    TRUE = "True"
    """Indicates the extension is enabled"""
    FALSE = "False"
    """Indicates the extension is disabled"""


class PricingTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The pricing tier value. Microsoft Defender for Cloud is provided in two pricing tiers: free and
    standard. The standard tier offers advanced security capabilities, while the free tier offers
    basic security features.
    """

    FREE = "Free"
    """Get free Microsoft Defender for Cloud experience with basic security features"""
    STANDARD = "Standard"
    """Get the standard Microsoft Defender for Cloud experience with advanced security features"""
