import dataclasses
from ..shared import error as shared_error
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class GetSchemasPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSchemasRequest:
    path_params: GetSchemasPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSchemasResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    schemata: Optional[list[shared_schema.Schema]] = dataclasses.field(default=None)
    