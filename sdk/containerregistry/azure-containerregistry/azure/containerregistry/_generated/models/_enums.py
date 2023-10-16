# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ArtifactArchitecture(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The artifact platform's architecture."""

    I386 = "386"
    """i386"""
    AMD64 = "amd64"
    """AMD64"""
    ARM = "arm"
    """ARM"""
    ARM64 = "arm64"
    """ARM64"""
    MIPS = "mips"
    """MIPS"""
    MIPS_LE = "mipsle"
    """MIPSLE"""
    MIPS64 = "mips64"
    """MIPS64"""
    MIPS64_LE = "mips64le"
    """MIPS64LE"""
    PPC64 = "ppc64"
    """PPC64"""
    PPC64_LE = "ppc64le"
    """PPC64LE"""
    RISC_V64 = "riscv64"
    """RISCv64"""
    S390_X = "s390x"
    """s390x"""
    WASM = "wasm"
    """Wasm"""


class ArtifactManifestOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sort options for ordering manifests in a collection."""

    NONE = "none"
    """Do not provide an orderby value in the request."""
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    """Order manifests by LastUpdatedOn field, from most recently updated to least recently updated."""
    LAST_UPDATED_ON_ASCENDING = "timeasc"
    """Order manifest by LastUpdatedOn field, from least recently updated to most recently updated."""


class ArtifactOperatingSystem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ArtifactOperatingSystem."""

    AIX = "aix"
    ANDROID = "android"
    DARWIN = "darwin"
    DRAGONFLY = "dragonfly"
    FREE_BSD = "freebsd"
    ILLUMOS = "illumos"
    I_OS = "ios"
    JS = "js"
    LINUX = "linux"
    NET_BSD = "netbsd"
    OPEN_BSD = "openbsd"
    PLAN9 = "plan9"
    SOLARIS = "solaris"
    WINDOWS = "windows"


class ArtifactTagOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sort options for ordering tags in a collection."""

    NONE = "none"
    """Do not provide an orderby value in the request."""
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    """Order tags by LastUpdatedOn field, from most recently updated to least recently updated."""
    LAST_UPDATED_ON_ASCENDING = "timeasc"
    """Order tags by LastUpdatedOn field, from least recently updated to most recently updated."""


class PostContentSchemaGrantType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Can take a value of access_token_refresh_token, or access_token, or refresh_token."""

    ACCESS_TOKEN_REFRESH_TOKEN = "access_token_refresh_token"
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"


class TokenGrantType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Grant type is expected to be refresh_token."""

    REFRESH_TOKEN = "refresh_token"
    PASSWORD = "password"
