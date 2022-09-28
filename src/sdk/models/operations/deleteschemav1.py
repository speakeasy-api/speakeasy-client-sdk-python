from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteSchemaV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteSchemaV1Request:
    path_params: DeleteSchemaV1PathParams = field(default=None)
    

@dataclass
class DeleteSchemaV1Responses:
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class DeleteSchemaV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, DeleteSchemaV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
