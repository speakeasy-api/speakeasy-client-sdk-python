import warnings
import requests
from typing import List,Optional
from sdk.models import operations, shared
from . import utils


SERVERS = [
	"https://api.prod.speakeasyapi.dev",
]


class SDK:
    client = requests.Session()
    server_url = SERVERS[0]

    def config_server_url(self, server_url: str, params: dict[str, str]):
        if not params is None:
            self.server_url = utils.replace_parameters(server_url, params)
        else:
            self.server_url = server_url
            
    
    def config_security(self, security: shared.Security):
        self.client = utils.configure_security_client(security)

    
    def delete_api(self, request: operations.DeleteAPIRequest) -> operations.DeleteAPIResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}", request.path_params)

        client = self.client

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

    
    def delete_api_endpoint(self, request: operations.DeleteAPIEndpointRequest) -> operations.DeleteAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)

        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def delete_schema(self, request: operations.DeleteSchemaRequest) -> operations.DeleteSchemaResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)

        client = self.client

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

    
    def delete_version_metadata(self, request: operations.DeleteVersionMetadataRequest) -> operations.DeleteVersionMetadataResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata/{metaKey}/{metaValue}", request.path_params)

        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteVersionMetadataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def download_schema(self, request: operations.DownloadSchemaRequest) -> operations.DownloadSchemaResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/download", request.path_params)

        client = self.client

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
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}/download", request.path_params)

        client = self.client

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

    
    def find_api_endpoint(self, request: operations.FindAPIEndpointRequest) -> operations.FindAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/find/{displayName}", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FindAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_open_api_spec(self, request: operations.GenerateOpenAPISpecRequest) -> operations.GenerateOpenAPISpecResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/openapi", request.path_params)

        client = self.client

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

    
    def generate_open_api_spec_for_api_endpoint(self, request: operations.GenerateOpenAPISpecForAPIEndpointRequest) -> operations.GenerateOpenAPISpecForAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/openapi", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GenerateOpenAPISpecForAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
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
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/postman", request.path_params)

        client = self.client

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

    
    def generate_postman_collection_for_api_endpoint(self, request: operations.GeneratePostmanCollectionForAPIEndpointRequest) -> operations.GeneratePostmanCollectionForAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/postman", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GeneratePostmanCollectionForAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bytes])
                res.postman_collection = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_request_postman_collection(self, request: operations.GenerateRequestPostmanCollectionRequest) -> operations.GenerateRequestPostmanCollectionResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/eventlog/{requestID}/generate/postman", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GenerateRequestPostmanCollectionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[bytes])
                res.postman_collection = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_api_endpoints(self, request: operations.GetAllAPIEndpointsRequest) -> operations.GetAllAPIEndpointsResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/api_endpoints", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIEndpointsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.APIEndpoint]])
                res.api_endpoints = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_api_versions(self, request: operations.GetAllAPIVersionsRequest) -> operations.GetAllAPIVersionsResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)

        query_params = utils.get_query_params(request.query_params)

        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIVersionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_for_version_api_endpoints(self, request: operations.GetAllForVersionAPIEndpointsRequest) -> operations.GetAllForVersionAPIEndpointsResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllForVersionAPIEndpointsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.APIEndpoint]])
                res.api_endpoints = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_api_endpoint(self, request: operations.GetAPIEndpointRequest) -> operations.GetAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_apis(self, request: operations.GetApisRequest) -> operations.GetApisResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = base_url.removesuffix("/") + "/v1/apis"

        query_params = utils.get_query_params(request.query_params)

        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetApisResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.API]])
                res.apis = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_embed_access_token(self, request: operations.GetEmbedAccessTokenRequest) -> operations.GetEmbedAccessTokenResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-token"

        query_params = utils.get_query_params(request.query_params)

        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEmbedAccessTokenResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.EmbedAccessTokenResponse])
                res.embed_access_token_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_request_from_event_log(self, request: operations.GetRequestFromEventLogRequest) -> operations.GetRequestFromEventLogResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/eventlog/{requestID}", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetRequestFromEventLogResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UnboundedRequest])
                res.unbounded_request = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_schema(self, request: operations.GetSchemaRequest) -> operations.GetSchemaResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)

        client = self.client

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
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{baseRevisionID}/diff/{targetRevisionID}", request.path_params)

        client = self.client

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
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)

        client = self.client

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
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schemas", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemasResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.Schema]])
                res.schemata = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_valid_embed_access_tokens(self) -> operations.GetValidEmbedAccessTokensResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-tokens/valid"

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetValidEmbedAccessTokensResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.EmbedToken]])
                res.embed_tokens = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_version_metadata(self, request: operations.GetVersionMetadataRequest) -> operations.GetVersionMetadataResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata", request.path_params)

        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVersionMetadataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.VersionMetadata]])
                res.version_metadata = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def insert_version_metadata(self, request: operations.InsertVersionMetadataRequest) -> operations.InsertVersionMetadataResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata", request.path_params)

        headers = {}

        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type

        if data is None and form is None:
           raise Exception('request body is required')

        client = self.client

        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InsertVersionMetadataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VersionMetadata])
                res.version_metadata = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def query_event_log(self, request: operations.QueryEventLogRequest) -> operations.QueryEventLogResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = base_url.removesuffix("/") + "/v1/eventlog/query"

        query_params = utils.get_query_params(request.query_params)

        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.QueryEventLogResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[List[shared.BoundedRequest]])
                res.bounded_requests = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def register_schema(self, request: operations.RegisterSchemaRequest) -> operations.RegisterSchemaResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)

        headers = {}

        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type

        if data is None and form is None:
           raise Exception('request body is required')

        client = self.client

        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RegisterSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def revoke_embed_access_token(self, request: operations.RevokeEmbedAccessTokenRequest) -> operations.RevokeEmbedAccessTokenResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/workspace/embed-access-tokens/{tokenID}", request.path_params)

        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RevokeEmbedAccessTokenResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def upsert_api(self, request: operations.UpsertAPIRequest) -> operations.UpsertAPIResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)

        headers = {}

        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type

        if data is None and form is None:
           raise Exception('request body is required')

        client = self.client

        r = client.request("PUT", url, data=data, files=form, headers=headers)
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

    
    def upsert_api_endpoint(self, request: operations.UpsertAPIEndpointRequest) -> operations.UpsertAPIEndpointResponse:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)

        headers = {}

        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type

        if data is None and form is None:
           raise Exception('request body is required')

        client = self.client

        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpsertAPIEndpointResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    