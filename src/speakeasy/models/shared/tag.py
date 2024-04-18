"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tag:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format {namespace_id}/{tag}"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human readable tag name"""
    namespace_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace_name') }})
    revision_digest: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revision_digest') }})
    
