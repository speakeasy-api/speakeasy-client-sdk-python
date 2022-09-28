from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteVersionMetadataV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    meta_key: str = field(default=None, metadata={'path_param': { 'field_name': 'metaKey', 'style': 'simple', 'explode': False }})
    meta_value: str = field(default=None, metadata={'path_param': { 'field_name': 'metaValue', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteVersionMetadataV1Request:
    path_params: DeleteVersionMetadataV1PathParams = field(default=None)
    

@dataclass
class DeleteVersionMetadataV1Responses:
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class DeleteVersionMetadataV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, DeleteVersionMetadataV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
