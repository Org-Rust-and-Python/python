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
    python firewalls_create_or_update_minimum_set_gen.py

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
            "location": "eastus",
            "properties": {
                "dnsSettings": {},
                "marketplaceDetails": {"offerId": "liftr-pan-ame-test", "publisherId": "isvtestuklegacy"},
                "networkProfile": {
                    "enableEgressNat": "ENABLED",
                    "networkType": "VNET",
                    "publicIps": [
                        {
                            "address": "20.22.92.11",
                            "resourceId": "/subscriptions/01c7d41f-afaf-464e-8a8b-5c6f9f98cee8/resourceGroups/mj-liftr-integration/providers/Microsoft.Network/publicIPAddresses/mj-liftr-integration-PublicIp1",
                        }
                    ],
                },
                "planData": {"billingCycle": "MONTHLY", "planId": "liftrpantestplan"},
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/paloaltonetworks/resource-manager/PaloAltoNetworks.Cloudngfw/preview/2022-08-29-preview/examples/Firewalls_CreateOrUpdate_MinimumSet_Gen.json
if __name__ == "__main__":
    main()
