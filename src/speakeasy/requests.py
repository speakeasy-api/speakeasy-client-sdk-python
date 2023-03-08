import requests as requests_http
from . import utils
from speakeasy.models import operations, shared
from typing import Optional

class Requests:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def generate_request_postman_collection(self, request: operations.GenerateRequestPostmanCollectionRequest) -> operations.GenerateRequestPostmanCollectionResponse:
        r"""Generate a Postman collection for a particular request.
        Generates a Postman collection for a particular request. 
        Allowing it to be replayed with the same inputs that were captured by the SDK.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/eventlog/{requestID}/generate/postman', request.path_params)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GenerateRequestPostmanCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.postman_collection = http_res.content
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def get_request_from_event_log(self, request: operations.GetRequestFromEventLogRequest) -> operations.GetRequestFromEventLogResponse:
        r"""Get information about a particular request.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/eventlog/{requestID}', request.path_params)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRequestFromEventLogResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UnboundedRequest])
                res.unbounded_request = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    def query_event_log(self, request: operations.QueryEventLogRequest) -> operations.QueryEventLogResponse:
        r"""Query the event log to retrieve a list of requests.
        Supports retrieving a list of request captured by the SDK for this workspace.
        Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/eventlog/query'
        
        headers = {}
        query_params = utils.get_query_params(request.query_params)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.QueryEventLogResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.BoundedRequest]])
                res.bounded_requests = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    