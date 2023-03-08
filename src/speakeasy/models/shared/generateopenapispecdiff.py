from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerateOpenAPISpecDiff:
    current_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_schema') }})
    new_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_schema') }})
    