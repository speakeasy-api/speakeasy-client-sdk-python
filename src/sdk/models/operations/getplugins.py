import dataclasses
from ..shared import error as shared_error
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class GetPluginsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    plugins: Optional[list[shared_plugin.Plugin]] = dataclasses.field(default=None)
    