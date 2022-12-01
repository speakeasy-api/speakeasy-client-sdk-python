from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class APIInput:
    r"""APIInput
    An Api is representation of a API (a collection of API Endpoints) within the Speakeasy Platform.
    """
    
    api_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    description: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    meta_data: Optional[dict[str, list[str]]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_data') }})
    

@dataclass_json
@dataclass
class API:
    r"""API
    An Api is representation of a API (a collection of API Endpoints) within the Speakeasy Platform.
    """
    
    api_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    updated_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    matched: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matched') }})
    meta_data: Optional[dict[str, list[str]]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_data') }})
    
