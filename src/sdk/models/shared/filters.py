from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from . import filter


@dataclass_json
@dataclass
class Filters:
    filters: List[filter.Filter] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'filters' }})
    limit: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'limit' }})
    offset: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'offset' }})
    operator: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'operator' }})
    
