import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclasses.dataclass
class GenerateOpenAPISpecDiff:
    current_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current_schema') }})
    new_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_schema') }})
    