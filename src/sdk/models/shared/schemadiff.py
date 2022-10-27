from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SchemaDiffValueChange:
    from_: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'From' }})
    to: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'To' }})
    

@dataclass_json
@dataclass
class SchemaDiff:
    additions: List[str] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'additions' }})
    deletions: List[str] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'deletions' }})
    modifications: dict[str, SchemaDiffValueChange] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'modifications' }})
    
