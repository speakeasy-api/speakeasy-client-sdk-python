from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class SchemaDiffValueChange:
    from_: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('From') }})
    to: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('To') }})
    

@dataclass_json
@dataclass
class SchemaDiff:
    r"""SchemaDiff
    A SchemaDiff represents a diff of two Schemas.
    """
    
    additions: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('additions') }})
    deletions: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deletions') }})
    modifications: dict[str, SchemaDiffValueChange] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifications') }})
    
