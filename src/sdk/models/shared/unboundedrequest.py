from dataclasses import dataclass, field
from datetime import datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UnboundedRequest:
    r"""UnboundedRequest
    An UnboundedRequest represents the HAR content capture by Speakeasy when logging a request.
    """
    created_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    har: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'har' }})
    har_size_bytes: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'har_size_bytes' }})
    request_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'request_id' }})
    workspace_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'workspace_id' }})
    
