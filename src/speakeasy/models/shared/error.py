from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from speakeasy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Error:
    r"""Error
    The `Status` type defines a logical error model
    """
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_code') }})
    