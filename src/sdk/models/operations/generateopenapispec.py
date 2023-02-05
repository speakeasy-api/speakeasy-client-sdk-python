import dataclasses
from ..shared import error as shared_error
from ..shared import generateopenapispecdiff as shared_generateopenapispecdiff
from typing import Optional


@dataclasses.dataclass
class GenerateOpenAPISpecPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GenerateOpenAPISpecRequest:
    path_params: GenerateOpenAPISpecPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GenerateOpenAPISpecResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    generate_open_api_spec_diff: Optional[shared_generateopenapispecdiff.GenerateOpenAPISpecDiff] = dataclasses.field(default=None)
    