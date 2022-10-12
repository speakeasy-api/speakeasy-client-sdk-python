from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetRequestFromEventLogPathParams:
    request_id: str = field(default=None, metadata={'path_param': { 'field_name': 'requestID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetRequestFromEventLogRequest:
    path_params: GetRequestFromEventLogPathParams = field(default=None)
    

@dataclass
class GetRequestFromEventLogResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    unbounded_request: Optional[shared.UnboundedRequest] = field(default=None)
    
