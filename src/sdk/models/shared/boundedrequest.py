from dataclasses import dataclass, field
from datetime import datetime
from marshmallow import fields
import dateutil.parser
from typing import List,Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BoundedRequest:
    api_endpoint_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'api_endpoint_id' }})
    api_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'api_id' }})
    created_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    customer_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'customer_id' }})
    latency: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'latency' }})
    metadata: Optional[dict[str, List[str]]] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'metadata' }})
    method: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'method' }})
    path: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'path' }})
    request_finish_time: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'request_finish_time', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    request_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'request_id' }})
    request_start_time: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'request_start_time', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'status' }})
    version_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'version_id' }})
    workspace_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'workspace_id' }})
    
