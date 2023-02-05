import dataclasses
from ..shared import filter as shared_filter
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclasses.dataclass
class Filters:
    r"""Filters
    Filters are used to query requests.
    """
    
    filters: list[shared_filter.Filter] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    operator: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operator') }})
    