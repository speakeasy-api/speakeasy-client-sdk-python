"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .interactiontype import InteractionType
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TargetSDKTypedDict(TypedDict):
    generate_gen_lock_id: str
    r"""gen.lock ID (expected to be a uuid). The same as `id`. A unique identifier for the target."""
    generate_target: str
    r"""eg `typescript`, `terraform`, `python`"""
    id: str
    r"""Unique identifier of the target the same as `generate_gen_lock_id`"""
    last_event_created_at: datetime
    r"""Timestamp when the event was created in the database."""
    last_event_id: str
    r"""Unique identifier of the last event for the target"""
    last_event_interaction_type: InteractionType
    r"""Type of interaction."""
    commit_head: NotRequired[str]
    r"""Remote commit ID."""
    continuous_integration_environment: NotRequired[str]
    r"""Name of the CI environment."""
    error: NotRequired[str]
    r"""Error message if the last event was not successful."""
    generate_config_post_version: NotRequired[str]
    r"""Version of the generated target (post generation)"""
    generate_eligible_features: NotRequired[str]
    r"""Eligible feature set during generation"""
    generate_gen_lock_pre_features: NotRequired[str]
    r"""Features prior to generation"""
    generate_gen_lock_pre_version: NotRequired[str]
    r"""Artifact version for the Previous Generation"""
    generate_number_of_operations_ignored: NotRequired[int]
    r"""The number of operations ignored in generation."""
    generate_number_of_operations_used: NotRequired[int]
    r"""The number of operations used in generation."""
    generate_number_of_terraform_resources: NotRequired[int]
    r"""The number of terraform resources used in generation."""
    generate_published: NotRequired[bool]
    r"""Indicates whether the target was considered published."""
    generate_target_name: NotRequired[str]
    r"""The workflow name of the target."""
    generate_target_version: NotRequired[str]
    r"""The version of the Speakeasy generator for this target eg v2 of the typescript generator."""
    gh_action_organization: NotRequired[str]
    r"""GitHub organization of the action."""
    gh_action_ref: NotRequired[str]
    r"""GitHub Action ref value."""
    gh_action_repository: NotRequired[str]
    r"""GitHub repository of the action."""
    gh_action_run_link: NotRequired[str]
    r"""Link to the GitHub action run."""
    gh_action_version: NotRequired[str]
    r"""Version of the GitHub action."""
    git_relative_cwd: NotRequired[str]
    r"""Current working directory relative to the git root."""
    git_remote_default_owner: NotRequired[str]
    r"""Default owner for git remote."""
    git_remote_default_repo: NotRequired[str]
    r"""Default repository name for git remote."""
    git_user_email: NotRequired[str]
    r"""User email from git configuration."""
    git_user_name: NotRequired[str]
    r"""User's name from git configuration. (not GitHub username)"""
    hostname: NotRequired[str]
    r"""Remote hostname."""
    last_publish_created_at: NotRequired[datetime]
    r"""Timestamp when the last publishing event was created."""
    last_publish_gh_action_run_link: NotRequired[str]
    r"""Link to the GitHub action run for the last publishing event."""
    publish_package_name: NotRequired[str]
    r"""Name of the published package."""
    publish_package_registry_name: NotRequired[str]
    r"""Name of the registry where the package was published."""
    publish_package_url: NotRequired[str]
    r"""URL of the published package."""
    publish_package_version: NotRequired[str]
    r"""Version of the published package."""
    repo_label: NotRequired[str]
    r"""Label of the git repository."""
    source_blob_digest: NotRequired[str]
    r"""The blob digest of the source."""
    source_namespace_name: NotRequired[str]
    r"""The namespace name of the source."""
    source_revision_digest: NotRequired[str]
    r"""The revision digest of the source."""
    success: NotRequired[bool]
    r"""Indicates whether the event was successful."""
    workflow_lock_post_raw: NotRequired[str]
    r"""Workflow lock file (post execution)"""
    workflow_lock_pre_raw: NotRequired[str]
    r"""Workflow lock file (prior to execution)"""
    workflow_post_raw: NotRequired[str]
    r"""Workflow file (post execution)"""
    workflow_pre_raw: NotRequired[str]
    r"""Workflow file (prior to execution)"""


class TargetSDK(BaseModel):
    generate_gen_lock_id: str
    r"""gen.lock ID (expected to be a uuid). The same as `id`. A unique identifier for the target."""

    generate_target: str
    r"""eg `typescript`, `terraform`, `python`"""

    id: str
    r"""Unique identifier of the target the same as `generate_gen_lock_id`"""

    last_event_created_at: datetime
    r"""Timestamp when the event was created in the database."""

    last_event_id: str
    r"""Unique identifier of the last event for the target"""

    last_event_interaction_type: InteractionType
    r"""Type of interaction."""

    commit_head: Optional[str] = None
    r"""Remote commit ID."""

    continuous_integration_environment: Optional[str] = None
    r"""Name of the CI environment."""

    error: Optional[str] = None
    r"""Error message if the last event was not successful."""

    generate_config_post_version: Optional[str] = None
    r"""Version of the generated target (post generation)"""

    generate_eligible_features: Optional[str] = None
    r"""Eligible feature set during generation"""

    generate_gen_lock_pre_features: Optional[str] = None
    r"""Features prior to generation"""

    generate_gen_lock_pre_version: Optional[str] = None
    r"""Artifact version for the Previous Generation"""

    generate_number_of_operations_ignored: Optional[int] = None
    r"""The number of operations ignored in generation."""

    generate_number_of_operations_used: Optional[int] = None
    r"""The number of operations used in generation."""

    generate_number_of_terraform_resources: Optional[int] = None
    r"""The number of terraform resources used in generation."""

    generate_published: Optional[bool] = None
    r"""Indicates whether the target was considered published."""

    generate_target_name: Optional[str] = None
    r"""The workflow name of the target."""

    generate_target_version: Optional[str] = None
    r"""The version of the Speakeasy generator for this target eg v2 of the typescript generator."""

    gh_action_organization: Optional[str] = None
    r"""GitHub organization of the action."""

    gh_action_ref: Optional[str] = None
    r"""GitHub Action ref value."""

    gh_action_repository: Optional[str] = None
    r"""GitHub repository of the action."""

    gh_action_run_link: Optional[str] = None
    r"""Link to the GitHub action run."""

    gh_action_version: Optional[str] = None
    r"""Version of the GitHub action."""

    git_relative_cwd: Optional[str] = None
    r"""Current working directory relative to the git root."""

    git_remote_default_owner: Optional[str] = None
    r"""Default owner for git remote."""

    git_remote_default_repo: Optional[str] = None
    r"""Default repository name for git remote."""

    git_user_email: Optional[str] = None
    r"""User email from git configuration."""

    git_user_name: Optional[str] = None
    r"""User's name from git configuration. (not GitHub username)"""

    hostname: Optional[str] = None
    r"""Remote hostname."""

    last_publish_created_at: Optional[datetime] = None
    r"""Timestamp when the last publishing event was created."""

    last_publish_gh_action_run_link: Optional[str] = None
    r"""Link to the GitHub action run for the last publishing event."""

    publish_package_name: Optional[str] = None
    r"""Name of the published package."""

    publish_package_registry_name: Optional[str] = None
    r"""Name of the registry where the package was published."""

    publish_package_url: Optional[str] = None
    r"""URL of the published package."""

    publish_package_version: Optional[str] = None
    r"""Version of the published package."""

    repo_label: Optional[str] = None
    r"""Label of the git repository."""

    source_blob_digest: Optional[str] = None
    r"""The blob digest of the source."""

    source_namespace_name: Optional[str] = None
    r"""The namespace name of the source."""

    source_revision_digest: Optional[str] = None
    r"""The revision digest of the source."""

    success: Optional[bool] = None
    r"""Indicates whether the event was successful."""

    workflow_lock_post_raw: Optional[str] = None
    r"""Workflow lock file (post execution)"""

    workflow_lock_pre_raw: Optional[str] = None
    r"""Workflow lock file (prior to execution)"""

    workflow_post_raw: Optional[str] = None
    r"""Workflow file (post execution)"""

    workflow_pre_raw: Optional[str] = None
    r"""Workflow file (prior to execution)"""
