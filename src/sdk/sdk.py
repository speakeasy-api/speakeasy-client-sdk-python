__doc__ = """ SDK Documentation: https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
import requests
from typing import Optional
from sdk.models import operations, shared
from . import utils


SERVERS = [
	"https://api.prod.speakeasyapi.dev",
]


class SDK:
    r"""SDK Documentation: https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
    client: requests.Session
    security_client: requests.Session
    security: shared.Security
    server_url = SERVERS[0]

    def __init__(self) -> None:
        self.client = requests.Session()
        self.security_client = requests.Session()


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if not params is None:
            self.server_url = utils.replace_parameters(server_url, params)
        else:
            self.server_url = server_url
    

    def config_client(self, client: requests.Session):
        self.client = client
        
        if self.security is not None:
            self.security_client = utils.configure_security_client(self.client, self.security)
        

    def config_security(self, security: shared.Security):
        self.security = security
        self.security_client = utils.configure_security_client(self.client, security)
    
    
    def delete_api(self, request: operations.DeleteAPIRequest) -> operations.DeleteAPIResponse:
        r"""Delete an Api.
        Delete a particular version of an Api. The will also delete all associated ApiEndpoints, Metadata, Schemas & Request Logs (if using a Postgres datastore).
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Delete an ApiEndpoint.
        Delete an ApiEndpoint. This will also delete all associated Request Logs (if using a Postgres datastore).
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Delete a particular schema revision for an Api.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Delete metadata for a particular apiID and versionID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata/{metaKey}/{metaValue}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Download the latest schema for a particular apiID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/download", request.path_params)
        
        
        client = self.security_client
        
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}/download", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Find an ApiEndpoint via its displayName.
        Find an ApiEndpoint via its displayName (set by operationId from a registered OpenAPI schema).
        This is useful for finding the ID of an ApiEndpoint to use in the /v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID} endpoints.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/find/{displayName}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Generate an OpenAPI specification for a particular Api.
        This endpoint will generate any missing operations in any registered OpenAPI document if the operation does not already exist in the document.
        Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/openapi", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Generate an OpenAPI specification for a particular ApiEndpoint.
        This endpoint will generate a new operation in any registered OpenAPI document if the operation does not already exist in the document.
        Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/openapi", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Generate a Postman collection for a particular Api.
        Generates a postman collection containing all endpoints for a particular API. Includes variables produced for any path/query/header parameters included in the OpenAPI document.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/generate/postman", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Generate a Postman collection for a particular ApiEndpoint.
        Generates a postman collection that allows the endpoint to be called from postman variables produced for any path/query/header parameters included in the OpenAPI document.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/postman", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Generate a Postman collection for a particular request.
        Generates a Postman collection for a particular request. 
        Allowing it to be replayed with the same inputs that were captured by the SDK.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/eventlog/{requestID}/generate/postman", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Get all Api endpoints for a particular apiID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/api_endpoints", request.path_params)
        
        
        client = self.security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIEndpointsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.APIEndpoint]])
                res.api_endpoints = out
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self.security_client
        
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

    
    def get_all_for_version_api_endpoints(self, request: operations.GetAllForVersionAPIEndpointsRequest) -> operations.GetAllForVersionAPIEndpointsResponse:
        r"""Get all ApiEndpoints for a particular apiID and versionID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints", request.path_params)
        
        
        client = self.security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllForVersionAPIEndpointsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.APIEndpoint]])
                res.api_endpoints = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_api_endpoint(self, request: operations.GetAPIEndpointRequest) -> operations.GetAPIEndpointResponse:
        r"""Get an ApiEndpoint.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Get a list of Apis for a given workspace
        Get a list of all Apis and their versions for a given workspace.
        Supports filtering the APIs based on metadata attributes.
        """
        
        base_url = self.server_url
        
        url = base_url.removesuffix("/") + "/v1/apis"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self.security_client
        
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

    
    def get_embed_access_token(self, request: operations.GetEmbedAccessTokenRequest) -> operations.GetEmbedAccessTokenResponse:
        r"""Get an embed access token for the current workspace.
        Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
        Filters can be applied allowing views to be filtered to things like particular customerIds.
        """
        
        base_url = self.server_url
        
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-token"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self.security_client
        
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
        r"""Get information about a particular request.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/eventlog/{requestID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Get information about the latest schema.
        Returns information about the last uploaded schema for a particular API version. 
        This won't include the schema itself, that can be retrieved via the downloadSchema operation.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        
        client = self.security_client
        
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{baseRevisionID}/diff/{targetRevisionID}", request.path_params)
        
        
        client = self.security_client
        
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        
        client = self.security_client
        
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schemas", request.path_params)
        
        
        client = self.security_client
        
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

    
    def get_valid_embed_access_tokens(self) -> operations.GetValidEmbedAccessTokensResponse:
        r"""Get all valid embed access tokens for the current workspace.
        """
        
        base_url = self.server_url
        
        url = base_url.removesuffix("/") + "/v1/workspace/embed-access-tokens/valid"
        
        
        client = self.security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetValidEmbedAccessTokensResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.EmbedToken]])
                res.embed_tokens = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_version_metadata(self, request: operations.GetVersionMetadataRequest) -> operations.GetVersionMetadataResponse:
        r"""Get all metadata for a particular apiID and versionID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata", request.path_params)
        
        
        client = self.security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVersionMetadataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.VersionMetadata]])
                res.version_metadata = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    
    def insert_version_metadata(self, request: operations.InsertVersionMetadataRequest) -> operations.InsertVersionMetadataResponse:
        r"""Insert metadata for a particular apiID and versionID.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/metadata", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.security_client
        
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
        r"""Query the event log to retrieve a list of requests.
        Supports retrieving a list of request captured by the SDK for this workspace.
        Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.
        """
        
        base_url = self.server_url
        
        url = base_url.removesuffix("/") + "/v1/eventlog/query"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self.security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.QueryEventLogResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.BoundedRequest]])
                res.bounded_requests = out
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
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.security_client
        
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
        r"""Revoke an embed access EmbedToken.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/workspace/embed-access-tokens/{tokenID}", request.path_params)
        
        
        client = self.security_client
        
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
        r"""Upsert an Api
        Upsert an Api. If the Api does not exist, it will be created.
        If the Api exists, it will be updated.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.security_client
        
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
        r"""Upsert an ApiEndpoint.
        Upsert an ApiEndpoint. If the ApiEndpoint does not exist it will be created, otherwise it will be updated.
        """
        
        base_url = self.server_url
        
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.security_client
        
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

    