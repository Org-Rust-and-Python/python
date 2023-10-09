# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.iothub import IotHubClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iothub
# USAGE
    python iothub_add_routing_cosmos_db_endpoint.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IotHubClient(
        credential=DefaultAzureCredential(),
        subscription_id="91d12660-3dec-467a-be2a-213b5544ddc0",
    )

    response = client.iot_hub_resource.begin_create_or_update(
        resource_group_name="myResourceGroup",
        resource_name="testHub",
        iot_hub_description={
            "etag": "AAAAAAFD6M4=",
            "location": "centraluseuap",
            "properties": {
                "cloudToDevice": {
                    "defaultTtlAsIso8601": "PT1H",
                    "feedback": {"lockDurationAsIso8601": "PT1M", "maxDeliveryCount": 10, "ttlAsIso8601": "PT1H"},
                    "maxDeliveryCount": 10,
                },
                "enableDataResidency": False,
                "enableFileUploadNotifications": False,
                "eventHubEndpoints": {"events": {"partitionCount": 2, "retentionTimeInDays": 1}},
                "features": "None",
                "ipFilterRules": [],
                "messagingEndpoints": {
                    "fileNotifications": {
                        "lockDurationAsIso8601": "PT1M",
                        "maxDeliveryCount": 10,
                        "ttlAsIso8601": "PT1H",
                    }
                },
                "minTlsVersion": "1.2",
                "networkRuleSets": {
                    "applyToBuiltInEventHubEndpoint": True,
                    "defaultAction": "Deny",
                    "ipRules": [
                        {"action": "Allow", "filterName": "rule1", "ipMask": "131.117.159.53"},
                        {"action": "Allow", "filterName": "rule2", "ipMask": "157.55.59.128/25"},
                    ],
                },
                "routing": {
                    "endpoints": {
                        "cosmosDBSqlContainers": [
                            {
                                "authenticationType": "keyBased",
                                "containerName": "test",
                                "databaseName": "systemstore",
                                "endpointUri": "https://test-systemstore-test2.documents.azure.com",
                                "name": "endpointcosmos",
                                "partitionKeyName": "keystamped",
                                "partitionKeyTemplate": "{deviceid}-{YYYY}-{MM}",
                                "primaryKey": "<primary-key>",
                                "resourceGroup": "rg-test",
                                "secondaryKey": "<secondary-key>",
                                "subscriptionId": "<subscription-id>",
                            }
                        ],
                        "eventHubs": [],
                        "serviceBusQueues": [],
                        "serviceBusTopics": [],
                        "storageContainers": [],
                    },
                    "fallbackRoute": {
                        "condition": "true",
                        "endpointNames": ["events"],
                        "isEnabled": True,
                        "name": "$fallback",
                        "source": "DeviceMessages",
                    },
                    "routes": [],
                },
                "storageEndpoints": {
                    "$default": {"connectionString": "", "containerName": "", "sasTtlAsIso8601": "PT1H"}
                },
            },
            "sku": {"capacity": 1, "name": "S1"},
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/iothub/resource-manager/Microsoft.Devices/stable/2023-06-30/examples/iothub_addRoutingCosmosDBEndpoint.json
if __name__ == "__main__":
    main()
