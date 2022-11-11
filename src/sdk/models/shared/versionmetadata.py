from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class VersionMetadata:
    r"""VersionMetadata
    A set of keys and associated values, attached to a particular version of an Api.
    """
    
    api_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    meta_key: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_key') }})
    meta_value: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_value') }})
    version_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    

@dataclass_json
@dataclass
class VersionMetadataInput:
    r"""VersionMetadataInput
    A set of keys and associated values, attached to a particular version of an Api.
    """
    
    meta_key: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_key') }})
    meta_value: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_value') }})
    
