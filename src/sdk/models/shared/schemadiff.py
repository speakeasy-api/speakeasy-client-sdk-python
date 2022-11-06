from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SchemaDiffValueChange:from_: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'From' }})
    to: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'To' }})
    

@dataclass_json
@dataclass
class SchemaDiff:
    r"""SchemaDiff
    A SchemaDiff represents a diff of two Schemas.
    """
    additions: list[str] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'additions' }})
    deletions: list[str] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'deletions' }})
    modifications: dict[str, SchemaDiffValueChange] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'modifications' }})
    
