# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ACLAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Azure Networking ACL Action."""

    ALLOW = "Allow"
    DENY = "Deny"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class FeatureFlags(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FeatureFlags is the supported features of Azure SignalR service.


    * ServiceMode: Flag for backend server for SignalR service. Values allowed: "Default": have
    your own backend server; "Serverless": your application doesn't have a backend server;
    "Classic": for backward compatibility. Support both Default and Serverless mode but not
    recommended; "PredefinedOnly": for future use.
    * EnableConnectivityLogs: "true"/"false", to enable/disable the connectivity log category
    respectively.
    * EnableMessagingLogs: "true"/"false", to enable/disable the connectivity log category
    respectively.
    * EnableLiveTrace: Live Trace allows you to know what's happening inside Azure SignalR service,
    it will give you live traces in real time, it will be helpful when you developing your own
    Azure SignalR based web application or self-troubleshooting some issues. Please note that live
    traces are counted as outbound messages that will be charged. Values allowed: "true"/"false",
    to enable/disable live trace feature.
    """

    SERVICE_MODE = "ServiceMode"
    ENABLE_CONNECTIVITY_LOGS = "EnableConnectivityLogs"
    ENABLE_MESSAGING_LOGS = "EnableMessagingLogs"
    ENABLE_LIVE_TRACE = "EnableLiveTrace"


class KeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of access key."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    SALT = "Salt"


class ManagedIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the identity type: systemAssigned, userAssigned, None."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class PrivateLinkServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the connection has been Approved/Rejected/Removed by the owner of the
    service.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"


class ScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scale type applicable to the sku."""

    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class ServiceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of the service."""

    SIGNAL_R = "SignalR"
    RAW_WEB_SOCKETS = "RawWebSockets"


class SharedPrivateLinkResourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the shared private link resource."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"


class SignalRRequestType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The incoming request type to the service."""

    CLIENT_CONNECTION = "ClientConnection"
    SERVER_CONNECTION = "ServerConnection"
    RESTAPI = "RESTAPI"
    TRACE = "Trace"


class SignalRSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Optional tier of this particular SKU. 'Standard' or 'Free'.

    ``Basic`` is deprecated, use ``Standard`` instead.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class UpstreamAuthType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Upstream auth type enum."""

    NONE = "None"
    MANAGED_IDENTITY = "ManagedIdentity"
