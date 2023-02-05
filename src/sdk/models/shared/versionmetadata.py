import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils


@dataclass_json
@dataclasses.dataclass
class VersionMetadataInput:
    r"""VersionMetadataInput
    A set of keys and associated values, attached to a particular version of an Api.
    """
    
    meta_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_key') }})
    meta_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_value') }})
    

@dataclass_json
@dataclasses.dataclass
class VersionMetadata:
    r"""VersionMetadata
    A set of keys and associated values, attached to a particular version of an Api.
    """
    
    api_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('api_id') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    meta_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_key') }})
    meta_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta_value') }})
    version_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('version_id') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace_id') }})
    