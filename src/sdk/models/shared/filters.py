from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from . import filter


@dataclass_json
@dataclass
class Filters:
    r"""Filters
    Filters are used to query requests.
    """
    filters: list[filter.Filter] = field(default=None, metadata={'dataclasses_json': { 'field_name': 'filters' }})
    limit: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'limit' }})
    offset: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'offset' }})
    operator: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'operator' }})
    
