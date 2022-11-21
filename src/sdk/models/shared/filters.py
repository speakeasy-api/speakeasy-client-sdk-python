from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from sdk import utils
from . import *


@dataclass_json
@dataclass
class Filters:
    r"""Filters
    Filters are used to query requests.
    """
    
    filters: List[Filter] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    limit: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: int = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    operator: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operator') }})
    
