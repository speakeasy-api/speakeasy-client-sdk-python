from dataclasses import dataclass, field
from datetime import datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class EmbedToken:
    r"""EmbedToken
    A representation of an embed token granted for working with Speakeasy components.
    """
    created_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_by' }})
    description: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'description' }})
    expires_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'expires_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    filters: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'filters' }})
    id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'id' }})
    last_used: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'last_used', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    revoked_at: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'revoked_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    revoked_by: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'revoked_by' }})
    workspace_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'workspace_id' }})
    
