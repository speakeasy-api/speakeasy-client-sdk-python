"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UnboundedRequest:
    r"""An UnboundedRequest represents the HAR content capture by Speakeasy when logging a request."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Creation timestamp."""
    har: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('har') }})
    r"""The HAR content of the request."""
    har_size_bytes: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('har_size_bytes') }})
    r"""The size of the HAR content in bytes."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""The ID of this request."""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    r"""The workspace ID this request was made to."""
    

