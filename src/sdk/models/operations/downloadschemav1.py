from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class DownloadSchemaV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DownloadSchemaV1Request:
    path_params: DownloadSchemaV1PathParams = field(default=None)
    

@dataclass
class DownloadSchemaV1Responses:
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class DownloadSchemaV1Response:
    content_type: str = field(default=None)
    headers: dict[str, List[str]] = field(default=None)
    responses: dict[int, dict[str, DownloadSchemaV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
