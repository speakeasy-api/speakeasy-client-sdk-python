from dataclasses import dataclass, field
from datetime import datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Schema:
    api_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'api_id' }})
    created_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'description' }})
    filename: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'filename' }})
    revision_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'revision_id' }})
    version_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'version_id' }})
    workspace_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'workspace_id' }})
    
