from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class RegisterSchemaPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class RegisterSchemaRequestBodyFile:
    content: bytes = field(metadata={'multipart_form': { 'content': True }})
    file: str = field(metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclass
class RegisterSchemaRequestBody:
    file: RegisterSchemaRequestBodyFile = field(metadata={'multipart_form': { 'file': True }})
    

@dataclass
class RegisterSchemaRequest:
    path_params: RegisterSchemaPathParams = field()
    request: RegisterSchemaRequestBody = field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclass
class RegisterSchemaResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    
