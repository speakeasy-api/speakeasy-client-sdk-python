from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Filter:
    r"""Filter
    A filter is a key-value pair that can be used to filter a list of requests.
    """
    key: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'key' }})
    operator: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'operator' }})
    value: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'value' }})
    
