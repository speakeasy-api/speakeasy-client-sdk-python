from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class BoundedRequest:
    r"""BoundedRequest
    A BoundedRequest is a request that has been logged by the Speakeasy without the contents of the request.
    """
    
    api_endpoint_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_endpoint_id') }})
    api_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    customer_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer_id') }})
    latency: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('latency') }})
    method: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('method') }})
    path: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('path') }})
    request_finish_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_finish_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    request_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_id') }})
    request_start_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    metadata: Optional[dict[str, list[str]]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    
