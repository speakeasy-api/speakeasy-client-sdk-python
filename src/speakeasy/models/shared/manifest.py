"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .annotations import Annotations
from .v2descriptor import V2Descriptor
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Manifest:
    r"""Returns the requested manifest file"""
    annotations: Optional[Annotations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('annotations'), 'exclude': lambda f: f is None }})
    r"""Annotations"""
    artifact_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('artifactType'), 'exclude': lambda f: f is None }})
    r"""Type of artifact"""
    layers: Optional[List[V2Descriptor]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layers'), 'exclude': lambda f: f is None }})
    r"""List of V2 image layer information"""
    media_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mediaType'), 'exclude': lambda f: f is None }})
    r"""Media type usually application/vnd.docker.distribution.manifest.v2+json if this is in the accept header"""
    schema_version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaVersion'), 'exclude': lambda f: f is None }})
    r"""Schema version"""
    

