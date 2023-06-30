# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import PolicyClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python create_policy_assignment_with_resource_selectors.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PolicyClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.policy_assignments.create(
        scope="subscriptions/ae640e6b-ba3e-4256-9d62-2993eecfa6f2",
        policy_assignment_name="CostManagement",
        parameters={
            "properties": {
                "description": "Limit the resource location and resource SKU",
                "displayName": "Limit the resource location and resource SKU",
                "metadata": {"assignedBy": "Special Someone"},
                "policyDefinitionId": "/subscriptions/ae640e6b-ba3e-4256-9d62-2993eecfa6f2/providers/Microsoft.Authorization/policySetDefinitions/CostManagement",
                "resourceSelectors": [
                    {
                        "name": "SDPRegions",
                        "selectors": [{"in": ["eastus2euap", "centraluseuap"], "kind": "resourceLocation"}],
                    }
                ],
            }
        },
    )
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2022-06-01/examples/createPolicyAssignmentWithResourceSelectors.json
if __name__ == "__main__":
    main()
