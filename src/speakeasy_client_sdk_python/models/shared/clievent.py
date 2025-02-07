"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .interactiontype import InteractionType
from datetime import datetime
from enum import Enum
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GenerateBumpType(str, Enum):
    r"""Bump type of the lock file (calculated semver delta, custom change (manual release), or prerelease/graduate)"""

    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
    CUSTOM = "custom"
    GRADUATE = "graduate"
    PRERELEASE = "prerelease"
    NONE = "none"


class OpenapiDiffBumpType(str, Enum):
    r"""Bump type of the lock file (calculated semver delta, or a custom change (manual release))"""

    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
    NONE = "none"


class CliEventTypedDict(TypedDict):
    created_at: datetime
    r"""Timestamp when the event was created in the database."""
    execution_id: str
    r"""Unique identifier for each execution of the CLI."""
    id: str
    r"""Unique identifier for each event."""
    interaction_type: InteractionType
    r"""Type of interaction."""
    local_started_at: datetime
    r"""Timestamp when the event started, in local time."""
    speakeasy_api_key_name: str
    r"""Identifier of the Speakeasy API key."""
    speakeasy_version: str
    r"""Version of the Speakeasy CLI."""
    success: bool
    r"""Indicates whether the event was successful."""
    workspace_id: str
    r"""Identifier of the workspace."""
    commit_head: NotRequired[str]
    r"""Remote commit ID."""
    continuous_integration_environment: NotRequired[str]
    r"""Name of the CI environment."""
    duration_ms: NotRequired[int]
    r"""Duration of the event in milliseconds."""
    error: NotRequired[str]
    r"""Error message if the event was not successful."""
    generate_bump_type: NotRequired[GenerateBumpType]
    r"""Bump type of the lock file (calculated semver delta, custom change (manual release), or prerelease/graduate)"""
    generate_config_post_checksum: NotRequired[str]
    r"""Checksum of the configuration file (post generation)"""
    generate_config_post_raw: NotRequired[str]
    r"""Rendered configuration file (post generation)"""
    generate_config_post_version: NotRequired[str]
    r"""The version of the customer's SDK that we just generated"""
    generate_config_pre_checksum: NotRequired[str]
    r"""Checksum of the configuration file (prior to generation)"""
    generate_config_pre_raw: NotRequired[str]
    r"""Rendered configuration file (prior to generation)"""
    generate_config_pre_version: NotRequired[str]
    r"""The version of the customer's SDK before we generated"""
    generate_eligible_features: NotRequired[str]
    r"""Eligible feature set during generation"""
    generate_gen_lock_id: NotRequired[str]
    r"""gen.lock ID (expected to be a uuid)."""
    generate_gen_lock_post_features: NotRequired[str]
    r"""Features post generation"""
    generate_gen_lock_pre_blob_digest: NotRequired[str]
    r"""Blob digest of the Previous Generation"""
    generate_gen_lock_pre_doc_checksum: NotRequired[str]
    r"""Checksum of the Previous Rendered OpenAPI document (prior to generation, via gen lock)"""
    generate_gen_lock_pre_doc_version: NotRequired[str]
    r"""info.Version of the Previous Rendered OpenAPI document (prior to generation, via gen lock)"""
    generate_gen_lock_pre_features: NotRequired[str]
    r"""Features prior to generation"""
    generate_gen_lock_pre_namespace_name: NotRequired[str]
    r"""Namespace name of the Previous Generation"""
    generate_gen_lock_pre_revision_digest: NotRequired[str]
    r"""Revision digest of the Previous Generation"""
    generate_gen_lock_pre_version: NotRequired[str]
    r"""Artifact version for the Previous Generation"""
    generate_number_of_operations_ignored: NotRequired[int]
    r"""The number of operations ignored in generation."""
    generate_number_of_operations_used: NotRequired[int]
    r"""The number of operations used in generation."""
    generate_number_of_terraform_resources: NotRequired[int]
    r"""The number of terraform resources used in generation."""
    generate_output_tests: NotRequired[bool]
    r"""Indicates whether tests were output."""
    generate_published: NotRequired[bool]
    r"""Indicates whether the target was considered published."""
    generate_repo_url: NotRequired[str]
    r"""Expected Repo URL, for use in documentation generation."""
    generate_target: NotRequired[str]
    r"""The target of the event."""
    generate_target_name: NotRequired[str]
    r"""The workflow name of the target."""
    generate_target_version: NotRequired[str]
    r"""The version of the target."""
    generate_version: NotRequired[str]
    r"""Version of the generation logic used."""
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
    gh_changes_committed: NotRequired[bool]
    r"""Whether or not changes were committed from generation in the Github Action."""
    gh_pull_request: NotRequired[str]
    r"""The reference to a created pull request URL."""
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
    last_step: NotRequired[str]
    r"""The last step of the event."""
    lint_report_digest: NotRequired[str]
    r"""The checksum of the lint report."""
    lint_report_error_count: NotRequired[int]
    r"""The number of errors in the lint report."""
    lint_report_info_count: NotRequired[int]
    r"""The number of info messages in the lint report."""
    lint_report_warning_count: NotRequired[int]
    r"""The number of warnings in the lint report."""
    local_completed_at: NotRequired[datetime]
    r"""Timestamp when the event completed, in local time."""
    management_doc_checksum: NotRequired[str]
    r"""Checksum of the currently Rendered OpenAPI document."""
    management_doc_version: NotRequired[str]
    r"""Version taken from info.version field of the Rendered OpenAPI document."""
    mermaid_diagram: NotRequired[str]
    r"""Mermaid diagram"""
    openapi_diff_base_source_blob_digest: NotRequired[str]
    r"""The blob digest of the base source."""
    openapi_diff_base_source_namespace_name: NotRequired[str]
    r"""The namespace name of the base source."""
    openapi_diff_base_source_revision_digest: NotRequired[str]
    r"""The revision digest of the base source."""
    openapi_diff_breaking_changes_count: NotRequired[int]
    r"""The number of breaking changes in the openapi diff report."""
    openapi_diff_bump_type: NotRequired[OpenapiDiffBumpType]
    r"""Bump type of the lock file (calculated semver delta, or a custom change (manual release))"""
    openapi_diff_report_digest: NotRequired[str]
    r"""The checksum of the openapi diff report."""
    publish_package_name: NotRequired[str]
    r"""Name of the published package."""
    publish_package_registry_name: NotRequired[str]
    r"""Name of the registry where the package was published."""
    publish_package_url: NotRequired[str]
    r"""URL of the published package."""
    publish_package_version: NotRequired[str]
    r"""Version of the published package."""
    raw_command: NotRequired[str]
    r"""Full CLI command."""
    repo_label: NotRequired[str]
    r"""Label of the git repository."""
    source_blob_digest: NotRequired[str]
    r"""The blob digest of the source."""
    source_namespace_name: NotRequired[str]
    r"""The namespace name of the source."""
    source_revision_digest: NotRequired[str]
    r"""The revision digest of the source."""
    workflow_lock_post_raw: NotRequired[str]
    r"""Workflow lock file (post execution)"""
    workflow_lock_pre_raw: NotRequired[str]
    r"""Workflow lock file (prior to execution)"""
    workflow_post_raw: NotRequired[str]
    r"""Workflow file (post execution)"""
    workflow_pre_raw: NotRequired[str]
    r"""Workflow file (prior to execution)"""


class CliEvent(BaseModel):
    created_at: datetime
    r"""Timestamp when the event was created in the database."""

    execution_id: str
    r"""Unique identifier for each execution of the CLI."""

    id: str
    r"""Unique identifier for each event."""

    interaction_type: InteractionType
    r"""Type of interaction."""

    local_started_at: datetime
    r"""Timestamp when the event started, in local time."""

    speakeasy_api_key_name: str
    r"""Identifier of the Speakeasy API key."""

    speakeasy_version: str
    r"""Version of the Speakeasy CLI."""

    success: bool
    r"""Indicates whether the event was successful."""

    workspace_id: str
    r"""Identifier of the workspace."""

    commit_head: Optional[str] = None
    r"""Remote commit ID."""

    continuous_integration_environment: Optional[str] = None
    r"""Name of the CI environment."""

    duration_ms: Optional[int] = None
    r"""Duration of the event in milliseconds."""

    error: Optional[str] = None
    r"""Error message if the event was not successful."""

    generate_bump_type: Optional[GenerateBumpType] = None
    r"""Bump type of the lock file (calculated semver delta, custom change (manual release), or prerelease/graduate)"""

    generate_config_post_checksum: Optional[str] = None
    r"""Checksum of the configuration file (post generation)"""

    generate_config_post_raw: Optional[str] = None
    r"""Rendered configuration file (post generation)"""

    generate_config_post_version: Optional[str] = None
    r"""The version of the customer's SDK that we just generated"""

    generate_config_pre_checksum: Optional[str] = None
    r"""Checksum of the configuration file (prior to generation)"""

    generate_config_pre_raw: Optional[str] = None
    r"""Rendered configuration file (prior to generation)"""

    generate_config_pre_version: Optional[str] = None
    r"""The version of the customer's SDK before we generated"""

    generate_eligible_features: Optional[str] = None
    r"""Eligible feature set during generation"""

    generate_gen_lock_id: Optional[str] = None
    r"""gen.lock ID (expected to be a uuid)."""

    generate_gen_lock_post_features: Optional[str] = None
    r"""Features post generation"""

    generate_gen_lock_pre_blob_digest: Optional[str] = None
    r"""Blob digest of the Previous Generation"""

    generate_gen_lock_pre_doc_checksum: Optional[str] = None
    r"""Checksum of the Previous Rendered OpenAPI document (prior to generation, via gen lock)"""

    generate_gen_lock_pre_doc_version: Optional[str] = None
    r"""info.Version of the Previous Rendered OpenAPI document (prior to generation, via gen lock)"""

    generate_gen_lock_pre_features: Optional[str] = None
    r"""Features prior to generation"""

    generate_gen_lock_pre_namespace_name: Optional[str] = None
    r"""Namespace name of the Previous Generation"""

    generate_gen_lock_pre_revision_digest: Optional[str] = None
    r"""Revision digest of the Previous Generation"""

    generate_gen_lock_pre_version: Optional[str] = None
    r"""Artifact version for the Previous Generation"""

    generate_number_of_operations_ignored: Optional[int] = None
    r"""The number of operations ignored in generation."""

    generate_number_of_operations_used: Optional[int] = None
    r"""The number of operations used in generation."""

    generate_number_of_terraform_resources: Optional[int] = None
    r"""The number of terraform resources used in generation."""

    generate_output_tests: Optional[bool] = None
    r"""Indicates whether tests were output."""

    generate_published: Optional[bool] = None
    r"""Indicates whether the target was considered published."""

    generate_repo_url: Optional[str] = None
    r"""Expected Repo URL, for use in documentation generation."""

    generate_target: Optional[str] = None
    r"""The target of the event."""

    generate_target_name: Optional[str] = None
    r"""The workflow name of the target."""

    generate_target_version: Optional[str] = None
    r"""The version of the target."""

    generate_version: Optional[str] = None
    r"""Version of the generation logic used."""

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

    gh_changes_committed: Optional[bool] = None
    r"""Whether or not changes were committed from generation in the Github Action."""

    gh_pull_request: Optional[str] = None
    r"""The reference to a created pull request URL."""

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

    last_step: Optional[str] = None
    r"""The last step of the event."""

    lint_report_digest: Optional[str] = None
    r"""The checksum of the lint report."""

    lint_report_error_count: Optional[int] = None
    r"""The number of errors in the lint report."""

    lint_report_info_count: Optional[int] = None
    r"""The number of info messages in the lint report."""

    lint_report_warning_count: Optional[int] = None
    r"""The number of warnings in the lint report."""

    local_completed_at: Optional[datetime] = None
    r"""Timestamp when the event completed, in local time."""

    management_doc_checksum: Optional[str] = None
    r"""Checksum of the currently Rendered OpenAPI document."""

    management_doc_version: Optional[str] = None
    r"""Version taken from info.version field of the Rendered OpenAPI document."""

    mermaid_diagram: Optional[str] = None
    r"""Mermaid diagram"""

    openapi_diff_base_source_blob_digest: Optional[str] = None
    r"""The blob digest of the base source."""

    openapi_diff_base_source_namespace_name: Optional[str] = None
    r"""The namespace name of the base source."""

    openapi_diff_base_source_revision_digest: Optional[str] = None
    r"""The revision digest of the base source."""

    openapi_diff_breaking_changes_count: Optional[int] = None
    r"""The number of breaking changes in the openapi diff report."""

    openapi_diff_bump_type: Optional[OpenapiDiffBumpType] = None
    r"""Bump type of the lock file (calculated semver delta, or a custom change (manual release))"""

    openapi_diff_report_digest: Optional[str] = None
    r"""The checksum of the openapi diff report."""

    publish_package_name: Optional[str] = None
    r"""Name of the published package."""

    publish_package_registry_name: Optional[str] = None
    r"""Name of the registry where the package was published."""

    publish_package_url: Optional[str] = None
    r"""URL of the published package."""

    publish_package_version: Optional[str] = None
    r"""Version of the published package."""

    raw_command: Optional[str] = None
    r"""Full CLI command."""

    repo_label: Optional[str] = None
    r"""Label of the git repository."""

    source_blob_digest: Optional[str] = None
    r"""The blob digest of the source."""

    source_namespace_name: Optional[str] = None
    r"""The namespace name of the source."""

    source_revision_digest: Optional[str] = None
    r"""The revision digest of the source."""

    workflow_lock_post_raw: Optional[str] = None
    r"""Workflow lock file (post execution)"""

    workflow_lock_pre_raw: Optional[str] = None
    r"""Workflow lock file (prior to execution)"""

    workflow_post_raw: Optional[str] = None
    r"""Workflow file (post execution)"""

    workflow_pre_raw: Optional[str] = None
    r"""Workflow file (prior to execution)"""
