from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchemaDiffValueChange:
    from_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('From') }})
    to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('To') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchemaDiff:
    r"""SchemaDiff
    A SchemaDiff represents a diff of two Schemas.
    """
    
    additions: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additions') }})
    deletions: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletions') }})
    modifications: dict[str, SchemaDiffValueChange] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifications') }})
    