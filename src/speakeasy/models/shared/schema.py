"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Schema:
    r"""A Schema represents an API schema for a particular Api and Version."""
    api_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_id') }})
    r"""The ID of the Api this Schema belongs to."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Creation timestamp."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""A detailed description of the Schema."""
    revision_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revision_id') }})
    r"""An ID referencing this particular revision of the Schema."""
    version_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version_id') }})
    r"""The version ID of the Api this Schema belongs to."""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    r"""The workspace ID this Schema belongs to."""
    

