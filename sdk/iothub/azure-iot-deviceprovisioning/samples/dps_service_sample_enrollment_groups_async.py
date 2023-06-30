# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: dps_service_sample_enrollment_groups_async.py
DESCRIPTION:
    This sample demos basic DPS enrollment group operations
PREREQUISITE:
    In order to create an x509 enrollment group, you'll need to have created at least
    one primary certificate. Any valid self-signed certificate should work.
     You can create a self-signed cert with openssl by running the following command:
        `openssl req -nodes -new -x509 -out enrollment-cert.pem --subj="/CN=Provisioning Service SDK Test Cert"`
USAGE: dps_service_sample_enrollment_groups.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_DPS_CONNECTION_STRING - the connection string to your DPS instance.
    2) AZURE_DPS_ENROLLMENT_CERT_PATH - Path to your certificate
"""

import asyncio
from os import environ


class EnrollmentGroupSamples(object):
    connection_string = environ["AZURE_DPS_CONNECTION_STRING"]
    x509_cert_path = environ["AZURE_DPS_ENROLLMENT_CERT_PATH"]

    symmetric_enrollment_group_id = "sample_symmetric_enrollment_group"
    x509_enrollment_group_id = "sample_x509_enrollment_group"

    async def create_symmetric_key_enrollment_group_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Create an enrollment group object with "SymmetricKey" attestation mechanism
        enrollment_group = {
            "enrollmentGroupId": self.symmetric_enrollment_group_id,
            "attestation": {
                "type": "symmetricKey",
            },
        }

        await dps_service_client.enrollment_group.create_or_update(
            id=self.symmetric_enrollment_group_id, enrollment_group=enrollment_group
        )

    async def create_x590_enrollment_group_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Load certificate contents from file
        certificate = open(self.x509_cert_path, "rt", encoding="utf-8")
        cert_contents = certificate.read()

        # Create an enrollment group object with "x509" attestation mechanism
        enrollment_group = {
            "enrollmentGroupId": self.x509_enrollment_group_id,
            "attestation": {
                "type": "x509",
                "x509": {
                    "signingCertificates": {
                        "primary": {"certificate": f"{cert_contents}"},
                        "secondary": {"certificate": f"{cert_contents}"},
                    }
                },
            },
        }

        await dps_service_client.enrollment_group.create_or_update(
            id=self.x509_enrollment_group_id, enrollment_group=enrollment_group
        )

    async def get_enrollment_group_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Get enrollment groups
        await dps_service_client.enrollment_group.get(
            id=self.symmetric_enrollment_group_id
        )

        await dps_service_client.enrollment_group.get(id=self.x509_enrollment_group_id)

    async def get_enrollment_group_attestation_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Get attestations for enrollment groups
        await dps_service_client.enrollment_group.get_attestation_mechanism(
            id=self.x509_enrollment_group_id
        )

        await dps_service_client.enrollment_group.get_attestation_mechanism(
            id=self.symmetric_enrollment_group_id
        )

    async def update_enrollment_group_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Get enrollment group
        sym_enrollment = await dps_service_client.enrollment_group.get(
            id=self.symmetric_enrollment_group_id
        )

        # Parse eTag to ensure update
        eTag = sym_enrollment["etag"]

        # Update enrollment group properties
        sym_enrollment["provisioningStatus"] = "disabled"
        sym_enrollment["allocationPolicy"] = "geoLatency"

        # Send update
        await dps_service_client.enrollment_group.create_or_update(
            id=self.symmetric_enrollment_group_id,
            enrollment_group=sym_enrollment,
            if_match=eTag,
        )

    async def bulk_enrollment_group_operations_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Create a few more enrollment groups in bulk
        enrollment_group_id = "bulk_enrollment_group_1"
        enrollment_group2_id = "bulk_enrollment_group_2"
        enrollment_groups = [
            # Create first enrollment
            {
                "enrollmentGroupId": enrollment_group_id,
                "attestation": {
                    "type": "symmetricKey",
                },
            },
            {
                "enrollmentGroupId": enrollment_group2_id,
                "attestation": {
                    "type": "symmetricKey",
                },
            },
        ]

        # Create a bulk operation object
        bulk_operation = {"mode": "create", "enrollmentGroups": enrollment_groups}

        # Send create operation
        await dps_service_client.enrollment_group.run_bulk_operation(
            bulk_operation=bulk_operation
        )

        # Modify bulk operation properties
        bulk_operation["mode"] = "delete"

        # Send delete operation
        await dps_service_client.enrollment_group.run_bulk_operation(
            bulk_operation=bulk_operation
        )

    async def delete_enrollment_groups_sample_async(self):
        # Instantiate a DPS Service Client using a connection string
        from azure.iot.deviceprovisioning.aio import DeviceProvisioningClient

        dps_service_client = DeviceProvisioningClient.from_connection_string(
            self.connection_string
        )

        # Delete enrollment groups
        await dps_service_client.enrollment_group.delete(
            id=self.x509_enrollment_group_id
        )
        await dps_service_client.enrollment_group.delete(
            id=self.symmetric_enrollment_group_id
        )


async def main():
    sample = EnrollmentGroupSamples()
    await sample.create_symmetric_key_enrollment_group_sample_async()
    await sample.create_x590_enrollment_group_sample_async()
    await sample.get_enrollment_group_sample_async()
    await sample.get_enrollment_group_attestation_sample_async()
    await sample.update_enrollment_group_sample_async()
    await sample.bulk_enrollment_group_operations_sample_async()
    await sample.delete_enrollment_groups_sample_async()


if __name__ == "__main__":
    asyncio.run(main())
