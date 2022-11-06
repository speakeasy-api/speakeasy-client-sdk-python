from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Error:
    r"""Error
    The `Status` type defines a logical error model
    """
    message: str = field(default=None, metadata={'dataclasses_json': { 'field_name': 'message' }})
    status_code: int = field(default=None, metadata={'dataclasses_json': { 'field_name': 'status_code' }})
    
