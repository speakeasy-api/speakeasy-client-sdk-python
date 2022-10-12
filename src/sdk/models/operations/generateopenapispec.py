from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GenerateOpenAPISpecPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GenerateOpenAPISpecRequest:
    path_params: GenerateOpenAPISpecPathParams = field(default=None)
    

@dataclass
class GenerateOpenAPISpecResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    generate_open_api_spec_diff: Optional[shared.GenerateOpenAPISpecDiff] = field(default=None)
    status_code: int = field(default=None)
    
