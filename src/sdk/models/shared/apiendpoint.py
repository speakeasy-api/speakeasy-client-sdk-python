from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class APIEndpoint:
    r"""APIEndpoint
    An ApiEndpoint is a description of an Endpoint for an API.
    """
    
    api_endpoint_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_endpoint_id') }})
    api_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    method: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('method') }})
    path: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('path') }})
    updated_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    matched: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched') }})
    

@dataclass_json
@dataclass
class APIEndpointInput:
    r"""APIEndpointInput
    An ApiEndpoint is a description of an Endpoint for an API.
    """
    
    api_endpoint_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_endpoint_id') }})
    description: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    display_name: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    method: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('method') }})
    path: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('path') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    
