from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteVersionMetadataPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    meta_key: str = field(default=None, metadata={'path_param': { 'field_name': 'metaKey', 'style': 'simple', 'explode': False }})
    meta_value: str = field(default=None, metadata={'path_param': { 'field_name': 'metaValue', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteVersionMetadataRequest:
    path_params: DeleteVersionMetadataPathParams = field(default=None)
    

@dataclass
class DeleteVersionMetadataResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
