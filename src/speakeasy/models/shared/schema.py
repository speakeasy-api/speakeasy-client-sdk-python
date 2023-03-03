from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Schema:
    r"""Schema
    A Schema represents an API schema for a particular Api and Version.
    """
    
    api_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_id') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    revision_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revision_id') }})
    version_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version_id') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    