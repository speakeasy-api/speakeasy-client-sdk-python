import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils


@dataclass_json
@dataclasses.dataclass
class UnboundedRequest:
    r"""UnboundedRequest
    An UnboundedRequest represents the HAR content capture by Speakeasy when logging a request.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    har: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('har') }})
    har_size_bytes: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('har_size_bytes') }})
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_id') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    