from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from sdk import utils
from . import filter


@dataclass_json
@dataclass
class Filters:
    r"""Filters
    Filters are used to query requests.
    """
    
    filters: list[filter.Filter] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    limit: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    operator: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operator') }})
    
