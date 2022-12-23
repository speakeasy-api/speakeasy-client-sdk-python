import requests
from typing import Optional
from sdk.models import shared, operations
from . import utils

class Apis:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def delete_api(self, request: operations.DeleteAPIRequest) -> operations.DeleteAPIResponse:
        r"""Delete an Api.
        Delete a particular version of an Api. The will also delete all associated ApiEndpoints, Metadata, Schemas & Request Logs (if using a Postgres datastore).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteAPIResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_open_api_spec(self, request: operations.GenerateOpenAPISpecRequest) -> operations.GenerateOpenAPISpecResponse:
        r"""Generate an OpenAPI specification for a particular Api.
        This endpoint will generate any missing operations in any registered OpenAPI document if the operation does not already exist in the document.
        Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/openapi", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GenerateOpenAPISpecResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.GenerateOpenAPISpecDiff])
                res.generate_open_api_spec_diff = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_postman_collection(self, request: operations.GeneratePostmanCollectionRequest) -> operations.GeneratePostmanCollectionResponse:
        r"""Generate a Postman collection for a particular Api.
        Generates a postman collection containing all endpoints for a particular API. Includes variables produced for any path/query/header parameters included in the OpenAPI document.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/postman", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GeneratePostmanCollectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bytes])
                res.postman_collection = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_api_versions(self, request: operations.GetAllAPIVersionsRequest) -> operations.GetAllAPIVersionsResponse:
        r"""Get all Api versions for a particular ApiEndpoint.
        Get all Api versions for a particular ApiEndpoint.
        Supports filtering the versions based on metadata attributes.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIVersionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_apis(self, request: operations.GetApisRequest) -> operations.GetApisResponse:
        r"""Get a list of Apis for a given workspace
        Get a list of all Apis and their versions for a given workspace.
        Supports filtering the APIs based on metadata attributes.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/v1/apis"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetApisResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def upsert_api(self, request: operations.UpsertAPIRequest) -> operations.UpsertAPIResponse:
        r"""Upsert an Api
        Upsert an Api. If the Api does not exist, it will be created.
        If the Api exists, it will be updated.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpsertAPIResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.API])
                res.api = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    