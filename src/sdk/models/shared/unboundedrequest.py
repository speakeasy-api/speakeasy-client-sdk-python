from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class UnboundedRequest:
    r"""UnboundedRequest
    An UnboundedRequest represents the HAR content capture by Speakeasy when logging a request.
    """
    
    created_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    har: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('har') }})
    har_size_bytes: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('har_size_bytes') }})
    request_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_id') }})
    workspace_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    
