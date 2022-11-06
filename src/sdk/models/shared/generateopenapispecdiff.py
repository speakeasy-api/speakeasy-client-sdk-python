from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GenerateOpenAPISpecDiff:current_schema: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'current_schema' }})
    new_schema: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'new_schema' }})
    
