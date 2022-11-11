from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class GenerateOpenAPISpecDiff:
    current_schema: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current_schema') }})
    new_schema: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_schema') }})
    
