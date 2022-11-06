from dataclasses import dataclass, field
from datetime import datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class VersionMetadata:
    r"""VersionMetadata
    A set of keys and associated values, attached to a particular version of an Api.
    """
    api_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'api_id' }})
    created_at: datetime = field(default=None, metadata={'dataclasses_json': { 'field_name': 'created_at', 'encoder': datetime.isoformat, 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    meta_key: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'meta_key' }})
    meta_value: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'meta_value' }})
    version_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'version_id' }})
    workspace_id: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'workspace_id' }})
    
