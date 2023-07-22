"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import filter as shared_filter
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Filters:
    r"""Filters are used to query requests."""
    filters: list[shared_filter.Filter] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters') }})
    r"""A list of filters to apply to the query."""
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""The maximum number of results to return."""
    offset: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset') }})
    r"""The offset to start the query from."""
    operator: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operator') }})
    r"""The operator to use when combining filters."""
    

