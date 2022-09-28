from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetSchemasV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemasV1Request:
    path_params: GetSchemasV1PathParams = field(default=None)
    

@dataclass
class GetSchemasV1Responses:
    error: Optional[shared.Error] = field(default=None)
    schemata: Optional[List[shared.Schema]] = field(default=None)
    

@dataclass
class GetSchemasV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetSchemasV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
