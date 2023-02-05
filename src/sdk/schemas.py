import requests
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Schemas:
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

    
    def delete_schema(self, request: operations.DeleteSchemaRequest) -> operations.DeleteSchemaResponse:
        r"""Delete a particular schema revision for an Api.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def download_schema(self, request: operations.DownloadSchemaRequest) -> operations.DownloadSchemaResponse:
        r"""Download the latest schema for a particular apiID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/download", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bytes])
                res.schema = out
            if utils.match_content_type(content_type, "application/x-yaml"):
                res.schema = r.content
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def download_schema_revision(self, request: operations.DownloadSchemaRevisionRequest) -> operations.DownloadSchemaRevisionResponse:
        r"""Download a particular schema revision for an Api.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}/download", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadSchemaRevisionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bytes])
                res.schema = out
            if utils.match_content_type(content_type, "application/x-yaml"):
                res.schema = r.content
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_schema(self, request: operations.GetSchemaRequest) -> operations.GetSchemaResponse:
        r"""Get information about the latest schema.
        Returns information about the last uploaded schema for a particular API version. 
        This won't include the schema itself, that can be retrieved via the downloadSchema operation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Schema])
                res.schema = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_schema_diff(self, request: operations.GetSchemaDiffRequest) -> operations.GetSchemaDiffResponse:
        r"""Get a diff of two schema revisions for an Api.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{baseRevisionID}/diff/{targetRevisionID}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaDiffResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SchemaDiff])
                res.schema_diff = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_schema_revision(self, request: operations.GetSchemaRevisionRequest) -> operations.GetSchemaRevisionResponse:
        r"""Get information about a particular schema revision for an Api.
        Returns information about the last uploaded schema for a particular schema revision. 
        This won't include the schema itself, that can be retrieved via the downloadSchema operation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaRevisionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Schema])
                res.schema = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_schemas(self, request: operations.GetSchemasRequest) -> operations.GetSchemasResponse:
        r"""Get information about all schemas associated with a particular apiID.
        Returns information the schemas associated with a particular apiID. 
        This won't include the schemas themselves, they can be retrieved via the downloadSchema operation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schemas", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemasResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.Schema]])
                res.schemata = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def register_schema(self, request: operations.RegisterSchemaRequest) -> operations.RegisterSchemaResponse:
        r"""Register a schema.
        Allows uploading a schema for a particular API version.
        This will be used to populate ApiEndpoints and used as a base for any schema generation if present.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RegisterSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    