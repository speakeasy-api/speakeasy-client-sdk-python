import dataclasses
from ..shared import error as shared_error
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class GetSchemaRevisionPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSchemaRevisionRequest:
    path_params: GetSchemaRevisionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSchemaRevisionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    