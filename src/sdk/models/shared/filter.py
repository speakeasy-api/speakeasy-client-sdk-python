from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Filter:
    key: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'key' }})
    operator: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'operator' }})
    value: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'value' }})
    
