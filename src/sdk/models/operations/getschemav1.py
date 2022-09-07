from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared

@dataclass
class GetSchemaV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaV1Request:
    path_params: GetSchemaV1PathParams = field(default=None)
    

@dataclass
class GetSchemaV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    schema: Optional[shared.Schema] = field(default=None)
    

@dataclass
class GetSchemaV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetSchemaV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
