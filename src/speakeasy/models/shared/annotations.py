"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Annotations:
    r"""Annotations"""
    org_opencontainers_image_authors: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.authors'), 'exclude': lambda f: f is None }})
    r"""The authors of the image"""
    org_opencontainers_image_created: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.created'), 'exclude': lambda f: f is None }})
    r"""The time the image was created"""
    org_opencontainers_image_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.description'), 'exclude': lambda f: f is None }})
    r"""Human-readable description of the software packaged in the image"""
    org_opencontainers_image_documentation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.documentation'), 'exclude': lambda f: f is None }})
    r"""The documentation URL of the image"""
    org_opencontainers_image_licenses: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.licenses'), 'exclude': lambda f: f is None }})
    org_opencontainers_image_ref_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.ref.name'), 'exclude': lambda f: f is None }})
    r"""Name of the reference for a target"""
    org_opencontainers_image_revision: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.revision'), 'exclude': lambda f: f is None }})
    r"""Source control revision identifier"""
    org_opencontainers_image_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.source'), 'exclude': lambda f: f is None }})
    r"""The URL to get source code for building the image"""
    org_opencontainers_image_title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.title'), 'exclude': lambda f: f is None }})
    r"""Human-readable title of the image"""
    org_opencontainers_image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.url'), 'exclude': lambda f: f is None }})
    r"""The URL of the image"""
    org_opencontainers_image_vendor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.vendor'), 'exclude': lambda f: f is None }})
    r"""Name of the distributing entity, organization or individual."""
    org_opencontainers_image_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org.opencontainers.image.version'), 'exclude': lambda f: f is None }})
    r"""The version of the packaged software"""
    

