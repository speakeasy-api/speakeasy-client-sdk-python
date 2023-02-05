import dataclasses
import dateutil.parser
from ..shared import requestmetadata as shared_requestmetadata
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class BoundedRequest:
    r"""BoundedRequest
    A BoundedRequest is a request that has been logged by the Speakeasy without the contents of the request.
    """
    
    api_endpoint_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_endpoint_id') }})
    api_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer_id') }})
    latency: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('latency') }})
    method: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('method') }})
    path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('path') }})
    request_finish_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_finish_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_id') }})
    request_start_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_start_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    version_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    metadata: Optional[list[shared_requestmetadata.RequestMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    