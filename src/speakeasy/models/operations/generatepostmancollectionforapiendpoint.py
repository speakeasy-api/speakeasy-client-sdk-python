from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointRequest:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    postman_collection: Optional[bytes] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    