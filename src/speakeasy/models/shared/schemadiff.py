"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils
from typing import Dict, List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchemaDiffValueChange:
    from_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('From') }})
    r"""Represents the previous value of the element."""
    to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('To') }})
    r"""Represents the current value of the element."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchemaDiff:
    r"""A SchemaDiff represents a diff of two Schemas."""
    additions: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additions') }})
    r"""Holds every addition change in the diff."""
    deletions: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletions') }})
    r"""Holds every deletion change in the diff."""
    modifications: Dict[str, SchemaDiffValueChange] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifications') }})
    r"""Holds every modification change in the diff."""
    

