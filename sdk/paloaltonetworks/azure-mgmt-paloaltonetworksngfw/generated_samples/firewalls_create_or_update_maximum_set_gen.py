# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.paloaltonetworksngfw import PaloAltoNetworksNgfwMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-paloaltonetworksngfw
# USAGE
    python firewalls_create_or_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PaloAltoNetworksNgfwMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="2bf4a339-294d-4c25-b0b2-ef649e9f5c27",
    )

    response = client.firewalls.begin_create_or_update(
        resource_group_name="firewall-rg",
        firewall_name="firewall1",
        resource={
            "identity": {
                "type": "None",
                "userAssignedIdentities": {"key16": {"clientId": "aaaa", "principalId": "aaaaaaaaaaaaaaa"}},
            },
            "location": "eastus",
            "properties": {
                "associatedRulestack": {"location": "eastus", "resourceId": "lrs1", "rulestackId": "PANRSID"},
                "dnsSettings": {
                    "dnsServers": [
                        {
                            "address": "20.22.92.111",
                            "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-egressNatIp1",
                        }
                    ],
                    "enableDnsProxy": "DISABLED",
                    "enabledDnsType": "CUSTOM",
                },
                "frontEndSettings": [
                    {
                        "backendConfiguration": {
                            "address": {
                                "address": "20.22.32.136",
                                "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-frontendSettingIp2",
                            },
                            "port": "80",
                        },
                        "frontendConfiguration": {
                            "address": {
                                "address": "20.22.91.251",
                                "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-frontendSettingIp1",
                            },
                            "port": "80",
                        },
                        "name": "frontendsetting11",
                        "protocol": "TCP",
                    }
                ],
                "isPanoramaManaged": "TRUE",
                "marketplaceDetails": {
                    "marketplaceSubscriptionStatus": "PendingFulfillmentStart",
                    "offerId": "liftr-pan-ame-test",
                    "publisherId": "isvtestuklegacy",
                },
                "networkProfile": {
                    "egressNatIp": [
                        {
                            "address": "20.22.92.111",
                            "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-egressNatIp1",
                        }
                    ],
                    "enableEgressNat": "ENABLED",
                    "networkType": "VNET",
                    "publicIps": [
                        {
                            "address": "20.22.92.11",
                            "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-PublicIp1",
                        }
                    ],
                    "vnetConfiguration": {
                        "ipOfTrustSubnetForUdr": {
                            "address": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-untrust-subnet",
                        },
                        "trustSubnet": {
                            "addressSpace": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-trust-subnet",
                        },
                        "unTrustSubnet": {
                            "addressSpace": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-untrust-subnet",
                        },
                        "vnet": {
                            "addressSpace": "10.1.0.0/16",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet",
                        },
                    },
                    "vwanConfiguration": {
                        "ipOfTrustSubnetForUdr": {
                            "address": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-untrust-subnet",
                        },
                        "networkVirtualApplianceId": "2bf4a339-294d-4c25-b0b2-ef649e9f5c12",
                        "trustSubnet": {
                            "addressSpace": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-trust-subnet",
                        },
                        "unTrustSubnet": {
                            "addressSpace": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-untrust-subnet",
                        },
                        "vHub": {
                            "addressSpace": "10.1.1.0/24",
                            "resourceId": "/subscriptions/2bf4a339-294d-4c25-b0b2-ef649e9f5c27/resourceGroups/os-liftr-integration/providers/Microsoft.Network/virtualNetworks/os-liftr-integration-vnet/subnets/os-liftr-integration-untrust-subnet",
                        },
                    },
                },
                "panEtag": "2bf4a339-294d-4c25-b0b2-ef649e9f5c12",
                "panoramaConfig": {"configString": "bas64EncodedString"},
                "planData": {"billingCycle": "MONTHLY", "planId": "liftrpantestplan", "usageType": "PAYG"},
                "provisioningState": "Accepted",
            },
            "tags": {"tagName": "value"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/preview/2022-08-29-preview/examples/Firewalls_CreateOrUpdate_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
