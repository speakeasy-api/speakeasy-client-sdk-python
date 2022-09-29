import warnings
import requests
from typing import List,Optional
from sdk.models import operations, shared
from . import utils


SERVERS = [
	"http://api.prod.speakeasyapi.dev",
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

    
    def delete_api_endpoint_v1(self, request: operations.DeleteAPIEndpointV1Request) -> operations.DeleteAPIEndpointV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteAPIEndpointV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DeleteAPIEndpointV1Responses(error=out)

        return res

    
    def delete_api_v1(self, request: operations.DeleteAPIV1Request) -> operations.DeleteAPIV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}", request.path_params)
        
        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteAPIV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DeleteAPIV1Responses(error=out)

        return res

    
    def delete_schema_v1(self, request: operations.DeleteSchemaV1Request) -> operations.DeleteSchemaV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteSchemaV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DeleteSchemaV1Responses(error=out)

        return res

    
    def delete_version_metadata_v1(self, request: operations.DeleteVersionMetadataV1Request) -> operations.DeleteVersionMetadataV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/versions/{versionID}/metadata/{metaKey}/{metaValue}", request.path_params)
        
        client = self.client

        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteVersionMetadataV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DeleteVersionMetadataV1Responses(error=out)

        return res

    
    def download_schema_revision_v1(self, request: operations.DownloadSchemaRevisionV1Request) -> operations.DownloadSchemaRevisionV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}/download", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadSchemaRevisionV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 302:
            res.headers = r.headers
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DownloadSchemaRevisionV1Responses(error=out)

        return res

    
    def download_schema_v1(self, request: operations.DownloadSchemaV1Request) -> operations.DownloadSchemaV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/download", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadSchemaV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 302:
            res.headers = r.headers
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.DownloadSchemaV1Responses(error=out)

        return res

    
    def find_api_endpoint_v1(self, request: operations.FindAPIEndpointV1Request) -> operations.FindAPIEndpointV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/find/{displayName}", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FindAPIEndpointV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.responses[r.status_code][content_type] = operations.FindAPIEndpointV1Responses(api_endpoint=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.FindAPIEndpointV1Responses(error=out)

        return res

    
    def get_all_api_endpoints_v1(self, request: operations.GetAllAPIEndpointsV1Request) -> operations.GetAllAPIEndpointsV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/api_endpoints", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIEndpointsV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.APIEndpoint]])
                res.responses[r.status_code][content_type] = operations.GetAllAPIEndpointsV1Responses(api_endpoints=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetAllAPIEndpointsV1Responses(error=out)

        return res

    
    def get_all_api_versions_v1(self, request: operations.GetAllAPIVersionsV1Request) -> operations.GetAllAPIVersionsV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllAPIVersionsV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.API]])
                res.responses[r.status_code][content_type] = operations.GetAllAPIVersionsV1Responses(apis=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetAllAPIVersionsV1Responses(error=out)

        return res

    
    def get_all_for_version_api_endpoints_v1(self, request: operations.GetAllForVersionAPIEndpointsV1Request) -> operations.GetAllForVersionAPIEndpointsV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllForVersionAPIEndpointsV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.APIEndpoint]])
                res.responses[r.status_code][content_type] = operations.GetAllForVersionAPIEndpointsV1Responses(api_endpoints=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetAllForVersionAPIEndpointsV1Responses(error=out)

        return res

    
    def get_api_endpoint_v1(self, request: operations.GetAPIEndpointV1Request) -> operations.GetAPIEndpointV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAPIEndpointV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.responses[r.status_code][content_type] = operations.GetAPIEndpointV1Responses(api_endpoint=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetAPIEndpointV1Responses(error=out)

        return res

    
    def get_apis_v1(self, request: operations.GetApisV1Request) -> operations.GetApisV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = base_url.removesuffix("/") + "/v1/apis"
        
        query_params = utils.get_query_params(request.query_params)
        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetApisV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.API]])
                res.responses[r.status_code][content_type] = operations.GetApisV1Responses(apis=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetApisV1Responses(error=out)

        return res

    
    def get_schema_diff_v1(self, request: operations.GetSchemaDiffV1Request) -> operations.GetSchemaDiffV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{baseRevisionID}/diff/{targetRevisionID}", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaDiffV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.SchemaDiff])
                res.responses[r.status_code][content_type] = operations.GetSchemaDiffV1Responses(schema_diff=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetSchemaDiffV1Responses(error=out)

        return res

    
    def get_schema_revision_v1(self, request: operations.GetSchemaRevisionV1Request) -> operations.GetSchemaRevisionV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaRevisionV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Schema])
                res.responses[r.status_code][content_type] = operations.GetSchemaRevisionV1Responses(schema=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetSchemaRevisionV1Responses(error=out)

        return res

    
    def get_schema_v1(self, request: operations.GetSchemaV1Request) -> operations.GetSchemaV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Schema])
                res.responses[r.status_code][content_type] = operations.GetSchemaV1Responses(schema=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetSchemaV1Responses(error=out)

        return res

    
    def get_schemas_v1(self, request: operations.GetSchemasV1Request) -> operations.GetSchemasV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schemas", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemasV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.Schema]])
                res.responses[r.status_code][content_type] = operations.GetSchemasV1Responses(schemata=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetSchemasV1Responses(error=out)

        return res

    
    def get_usage_metrics_v1(self, request: operations.GetUsageMetricsV1Request) -> operations.GetUsageMetricsV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/workspace/{workspaceID}/metrics", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        client = self.client

        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUsageMetricsV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.UsageMetric]])
                res.responses[r.status_code][content_type] = operations.GetUsageMetricsV1Responses(usage_metrics=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetUsageMetricsV1Responses(error=out)

        return res

    
    def get_version_metadata_v1(self, request: operations.GetVersionMetadataV1Request) -> operations.GetVersionMetadataV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/versions/{versionID}/metadata", request.path_params)
        
        client = self.client

        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVersionMetadataV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[List[shared.VersionMetadata]])
                res.responses[r.status_code][content_type] = operations.GetVersionMetadataV1Responses(version_metadata=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.GetVersionMetadataV1Responses(error=out)

        return res

    
    def insert_version_metadata_v1(self, request: operations.InsertVersionMetadataV1Request) -> operations.InsertVersionMetadataV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/versions/{versionID}/metadata", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.client

        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InsertVersionMetadataV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.VersionMetadata])
                res.responses[r.status_code][content_type] = operations.InsertVersionMetadataV1Responses(version_metadata=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.InsertVersionMetadataV1Responses(error=out)

        return res

    
    def register_schema_v1(self, request: operations.RegisterSchemaV1Request) -> operations.RegisterSchemaV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.client

        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RegisterSchemaV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.RegisterSchemaV1Responses(error=out)

        return res

    
    def upsert_api_endpoint_v1(self, request: operations.UpsertAPIEndpointV1Request) -> operations.UpsertAPIEndpointV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.client

        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpsertAPIEndpointV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.APIEndpoint])
                res.responses[r.status_code][content_type] = operations.UpsertAPIEndpointV1Responses(api_endpoint=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.UpsertAPIEndpointV1Responses(error=out)

        return res

    
    def upsert_api_v1(self, request: operations.UpsertAPIV1Request) -> operations.UpsertAPIV1Response:
        warnings.simplefilter("ignore")

        base_url = self.server_url
        url = utils.generate_url(base_url, "/v1/apis/{apiID}", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self.client

        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpsertAPIV1Response(status_code=r.status_code, content_type=content_type, responses={r.status_code: {content_type: {}}})
        if r.status_code == 200:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.API])
                res.responses[r.status_code][content_type] = operations.UpsertAPIV1Responses(api=out)
        else:
            if content_type == "application/json; charset=UTF-8":
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.responses[r.status_code][content_type] = operations.UpsertAPIV1Responses(error=out)

        return res

    