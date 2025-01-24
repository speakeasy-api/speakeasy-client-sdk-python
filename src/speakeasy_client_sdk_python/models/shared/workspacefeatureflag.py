"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from speakeasy_client_sdk_python import utils


class WorkspaceFeatureFlag(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""enum value workspace feature flag"""

    SCHEMA_REGISTRY = "schema_registry"
    CHANGES_REPORT = "changes_report"
    SKIP_SCHEMA_REGISTRY = "skip_schema_registry"
    WEBHOOKS = "webhooks"
