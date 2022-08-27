from dataclasses import dataclass, field
from typing import List,Optional
from .error import Error

@dataclass
class DownloadSchemaRevisionV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DownloadSchemaRevisionV1Request:
    path_params: DownloadSchemaRevisionV1PathParams = field(default=None)
    

@dataclass
class DownloadSchemaRevisionV1Responses:
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class DownloadSchemaRevisionV1Response:
    content_type: str = field(default=None)
    headers: dict[str, List[str]] = field(default=None)
    responses: dict[int, dict[str, DownloadSchemaRevisionV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
