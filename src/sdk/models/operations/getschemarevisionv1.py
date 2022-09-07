from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared

@dataclass
class GetSchemaRevisionV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaRevisionV1Request:
    path_params: GetSchemaRevisionV1PathParams = field(default=None)
    

@dataclass
class GetSchemaRevisionV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    schema: Optional[shared.Schema] = field(default=None)
    

@dataclass
class GetSchemaRevisionV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetSchemaRevisionV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
