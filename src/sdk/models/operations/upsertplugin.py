import dataclasses
from ..shared import error as shared_error
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class UpsertPluginRequest:
    request: shared_plugin.Plugin = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpsertPluginResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    plugin: Optional[shared_plugin.Plugin] = dataclasses.field(default=None)
    