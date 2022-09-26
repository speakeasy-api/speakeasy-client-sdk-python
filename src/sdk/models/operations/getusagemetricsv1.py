from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetUsageMetricsV1PathParams:
    workspace_id: str = field(default=None, metadata={'path_param': { 'field_name': 'workspaceID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetUsageMetricsV1QueryParams:
    filters: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'filters', 'style': 'form', 'explode': True }})
    

@dataclass
class GetUsageMetricsV1Request:
    path_params: GetUsageMetricsV1PathParams = field(default=None)
    query_params: GetUsageMetricsV1QueryParams = field(default=None)
    

@dataclass
class GetUsageMetricsV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    usage_metric: Optional[List[shared.UsageMetric]] = field(default=None)
    

@dataclass
class GetUsageMetricsV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetUsageMetricsV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
