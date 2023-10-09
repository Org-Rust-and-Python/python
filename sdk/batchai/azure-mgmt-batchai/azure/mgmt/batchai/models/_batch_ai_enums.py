# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AllocationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allocation state of the cluster. Possible values are: steady - Indicates that the cluster is
    not resizing. There are no changes to the number of compute nodes in the cluster in progress. A
    cluster enters this state when it is created and when no operations are being performed on the
    cluster to change the number of compute nodes. resizing - Indicates that the cluster is
    resizing; that is, compute nodes are being added to or removed from the cluster.
    """

    STEADY = "steady"
    RESIZING = "resizing"

class CachingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Caching type for the disks. Available values are none (default), readonly, readwrite. Caching
    type can be set only for VM sizes supporting premium storage.
    """

    NONE = "none"
    READONLY = "readonly"
    READWRITE = "readwrite"

class DeallocationOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Actions which should be performed when compute nodes are removed from the cluster. Possible
    values are: requeue (default) - Terminate running jobs and requeue them so the jobs will run
    again. Remove compute nodes as soon as jobs have been terminated; terminate - Terminate running
    jobs. The jobs will not run again. Remove compute nodes as soon as jobs have been terminated.
    waitforjobcompletion - Allow currently running jobs to complete. Schedule no new jobs while
    waiting. Remove compute nodes when all jobs have completed.
    """

    REQUEUE = "requeue"
    TERMINATE = "terminate"
    WAITFORJOBCOMPLETION = "waitforjobcompletion"

class ExecutionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the job. Possible values are: queued - The job is queued and able to run.
    A job enters this state when it is created, or when it is awaiting a retry after a failed run.
    running - The job is running on a compute cluster. This includes job-level preparation such as
    downloading resource files or set up container specified on the job - it does not necessarily
    mean that the job command line has started executing. terminating - The job is terminated by
    the user, the terminate operation is in progress. succeeded - The job has completed running
    successfully and exited with exit code 0. failed - The job has finished unsuccessfully (failed
    with a non-zero exit code) and has exhausted its retry limit. A job is also marked as failed if
    an error occurred launching the job.
    """

    QUEUED = "queued"
    RUNNING = "running"
    TERMINATING = "terminating"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

class FileServerProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the File Server. Possible values: creating - The File Server is getting
    created; updating - The File Server creation has been accepted and it is getting updated;
    deleting - The user has requested that the File Server be deleted, and it is in the process of
    being deleted; failed - The File Server creation has failed with the specified error code.
    Details about the error code are specified in the message field; succeeded - The File Server
    creation has succeeded.
    """

    CREATING = "creating"
    UPDATING = "updating"
    DELETING = "deleting"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

class FileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the file. Possible values are file and directory.
    """

    FILE = "file"
    DIRECTORY = "directory"

class JobPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scheduling priority associated with the job. Possible values: low, normal, high.
    """

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the cluster. Possible value are: creating - Specifies that the cluster is
    being created. succeeded - Specifies that the cluster has been created successfully. failed -
    Specifies that the cluster creation has failed. deleting - Specifies that the cluster is being
    deleted.
    """

    CREATING = "creating"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    DELETING = "deleting"

class StorageAccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of storage account to be used on the disk. Possible values are: Standard_LRS or
    Premium_LRS. Premium storage account type can only be used with VM sizes supporting premium
    storage.
    """

    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"

class ToolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The toolkit type of the job.
    """

    CNTK = "cntk"
    TENSORFLOW = "tensorflow"
    CAFFE = "caffe"
    CAFFE2 = "caffe2"
    CHAINER = "chainer"
    HOROVOD = "horovod"
    CUSTOMMPI = "custommpi"
    CUSTOM = "custom"

class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enum describing the unit of usage measurement.
    """

    COUNT = "Count"

class VmPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VM priority. Allowed values are: dedicated (default) and lowpriority.
    """

    DEDICATED = "dedicated"
    LOWPRIORITY = "lowpriority"
