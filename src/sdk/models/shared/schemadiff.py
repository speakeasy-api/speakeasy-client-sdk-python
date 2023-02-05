import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclasses.dataclass
class SchemaDiffValueChange:
    from_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('From') }})
    to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('To') }})
    

@dataclass_json
@dataclasses.dataclass
class SchemaDiff:
    r"""SchemaDiff
    A SchemaDiff represents a diff of two Schemas.
    """
    
    additions: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('additions') }})
    deletions: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deletions') }})
    modifications: dict[str, SchemaDiffValueChange] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifications') }})
    