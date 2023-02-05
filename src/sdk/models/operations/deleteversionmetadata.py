import dataclasses
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class DeleteVersionMetadataPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    meta_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metaKey', 'style': 'simple', 'explode': False }})
    meta_value: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metaValue', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteVersionMetadataRequest:
    path_params: DeleteVersionMetadataPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteVersionMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    