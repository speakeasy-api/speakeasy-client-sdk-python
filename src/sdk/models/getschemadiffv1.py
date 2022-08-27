from dataclasses import dataclass, field
from typing import Optional
from .error import Error
from .schemadiff import SchemaDiff

@dataclass
class GetSchemaDiffV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    base_revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'baseRevisionID', 'style': 'simple', 'explode': False }})
    target_revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'targetRevisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaDiffV1Request:
    path_params: GetSchemaDiffV1PathParams = field(default=None)
    

@dataclass
class GetSchemaDiffV1Responses:
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    schema_diff: Optional[SchemaDiff] = field(default=None)
    

@dataclass
class GetSchemaDiffV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetSchemaDiffV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
