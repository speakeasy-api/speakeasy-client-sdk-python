import cgi
import warnings
from typing import List, Optional

import requests

from . import models
from . import utils

SERVER_URL = "http://api.prod.speakeasyapi.dev"

class SDK:
    client: requests.Session = requests.Session()

    
    def config_security(self, security: models.Security):
        utils.configure_security_client(self.client, security)

    
    def delete_api_endpoint_v1(self, request: models.DeleteAPIEndpointV1Request) -> models.DeleteAPIEndpointV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        

        r = self.client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DeleteAPIEndpointV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DeleteAPIEndpointV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DeleteAPIEndpointV1Responses(raw_response=r.content)

        return res

    
    def delete_api_v1(self, request: models.DeleteAPIV1Request) -> models.DeleteAPIV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}", request.path_params)
        

        r = self.client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DeleteAPIV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DeleteAPIV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DeleteAPIV1Responses(raw_response=r.content)

        return res

    
    def delete_schema_v1(self, request: models.DeleteSchemaV1Request) -> models.DeleteSchemaV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        

        r = self.client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DeleteSchemaV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DeleteSchemaV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DeleteSchemaV1Responses(raw_response=r.content)

        return res

    
    def delete_version_metadata_v1(self, request: models.DeleteVersionMetadataV1Request) -> models.DeleteVersionMetadataV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/versions/{versionID}/metadata/{metaKey}/{metaValue}", request.path_params)
        

        r = self.client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DeleteVersionMetadataV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DeleteVersionMetadataV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DeleteVersionMetadataV1Responses(raw_response=r.content)

        return res

    
    def download_schema_revision_v1(self, request: models.DownloadSchemaRevisionV1Request) -> models.DownloadSchemaRevisionV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}/download", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DownloadSchemaRevisionV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 302:
            res.headers = r.headers
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DownloadSchemaRevisionV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DownloadSchemaRevisionV1Responses(raw_response=r.content)

        return res

    
    def download_schema_v1(self, request: models.DownloadSchemaV1Request) -> models.DownloadSchemaV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema/download", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.DownloadSchemaV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 302:
            res.headers = r.headers
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.DownloadSchemaV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.DownloadSchemaV1Responses(raw_response=r.content)

        return res

    
    def find_api_endpoint_v1(self, request: models.FindAPIEndpointV1Request) -> models.FindAPIEndpointV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/find/{displayName}", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.FindAPIEndpointV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.APIEndpoint])
                res.responses[r.status_code][mime_type] = models.FindAPIEndpointV1Responses(api_endpoint=out)
            else:
                res.responses[r.status_code][mime_type] = models.FindAPIEndpointV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.FindAPIEndpointV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.FindAPIEndpointV1Responses(raw_response=r.content)

        return res

    
    def get_all_api_endpoints_v1(self, request: models.GetAllAPIEndpointsV1Request) -> models.GetAllAPIEndpointsV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/api_endpoints", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetAllAPIEndpointsV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.APIEndpoint]])
                res.responses[r.status_code][mime_type] = models.GetAllAPIEndpointsV1Responses(api_endpoint=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllAPIEndpointsV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetAllAPIEndpointsV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllAPIEndpointsV1Responses(raw_response=r.content)

        return res

    
    def get_all_api_versions_v1(self, request: models.GetAllAPIVersionsV1Request) -> models.GetAllAPIVersionsV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)

        r = self.client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetAllAPIVersionsV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.API]])
                res.responses[r.status_code][mime_type] = models.GetAllAPIVersionsV1Responses(api=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllAPIVersionsV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetAllAPIVersionsV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllAPIVersionsV1Responses(raw_response=r.content)

        return res

    
    def get_all_for_version_api_endpoints_v1(self, request: models.GetAllForVersionAPIEndpointsV1Request) -> models.GetAllForVersionAPIEndpointsV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/api_endpoints", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetAllForVersionAPIEndpointsV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.APIEndpoint]])
                res.responses[r.status_code][mime_type] = models.GetAllForVersionAPIEndpointsV1Responses(api_endpoint=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllForVersionAPIEndpointsV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetAllForVersionAPIEndpointsV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAllForVersionAPIEndpointsV1Responses(raw_response=r.content)

        return res

    
    def get_api_endpoint_v1(self, request: models.GetAPIEndpointV1Request) -> models.GetAPIEndpointV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetAPIEndpointV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.APIEndpoint])
                res.responses[r.status_code][mime_type] = models.GetAPIEndpointV1Responses(api_endpoint=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAPIEndpointV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetAPIEndpointV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetAPIEndpointV1Responses(raw_response=r.content)

        return res

    
    def get_apis_v1(self, request: models.GetApisV1Request) -> models.GetApisV1Response:
        warnings.simplefilter("ignore")
        url = SERVER_URL.removesuffix("/") + "/v1/apis"
        
        query_params = utils.get_query_params(request.query_params)

        r = self.client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetApisV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.API]])
                res.responses[r.status_code][mime_type] = models.GetApisV1Responses(api=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetApisV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetApisV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetApisV1Responses(raw_response=r.content)

        return res

    
    def get_schema_diff_v1(self, request: models.GetSchemaDiffV1Request) -> models.GetSchemaDiffV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema/{baseRevisionID}/diff/{targetRevisionID}", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetSchemaDiffV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.SchemaDiff])
                res.responses[r.status_code][mime_type] = models.GetSchemaDiffV1Responses(schema_diff=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaDiffV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetSchemaDiffV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaDiffV1Responses(raw_response=r.content)

        return res

    
    def get_schema_revision_v1(self, request: models.GetSchemaRevisionV1Request) -> models.GetSchemaRevisionV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema/{revisionID}", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetSchemaRevisionV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Schema])
                res.responses[r.status_code][mime_type] = models.GetSchemaRevisionV1Responses(schema=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaRevisionV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetSchemaRevisionV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaRevisionV1Responses(raw_response=r.content)

        return res

    
    def get_schema_v1(self, request: models.GetSchemaV1Request) -> models.GetSchemaV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetSchemaV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Schema])
                res.responses[r.status_code][mime_type] = models.GetSchemaV1Responses(schema=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetSchemaV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemaV1Responses(raw_response=r.content)

        return res

    
    def get_schemas_v1(self, request: models.GetSchemasV1Request) -> models.GetSchemasV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schemas", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetSchemasV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.Schema]])
                res.responses[r.status_code][mime_type] = models.GetSchemasV1Responses(schema=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemasV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetSchemasV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetSchemasV1Responses(raw_response=r.content)

        return res

    
    def get_version_metadata_v1(self, request: models.GetVersionMetadataV1Request) -> models.GetVersionMetadataV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/versions/{versionID}/metadata", request.path_params)
        

        r = self.client.request("GET", url)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.GetVersionMetadataV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[List[models.VersionMetadata]])
                res.responses[r.status_code][mime_type] = models.GetVersionMetadataV1Responses(version_metadata=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetVersionMetadataV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.GetVersionMetadataV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.GetVersionMetadataV1Responses(raw_response=r.content)

        return res

    
    def insert_version_metadata_v1(self, request: models.InsertVersionMetadataV1Request) -> models.InsertVersionMetadataV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/versions/{versionID}/metadata", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        

        r = self.client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.InsertVersionMetadataV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.VersionMetadata])
                res.responses[r.status_code][mime_type] = models.InsertVersionMetadataV1Responses(version_metadata=out)
            else:
                res.responses[r.status_code][mime_type] = models.InsertVersionMetadataV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.InsertVersionMetadataV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.InsertVersionMetadataV1Responses(raw_response=r.content)

        return res

    
    def register_schema_v1(self, request: models.RegisterSchemaV1Request) -> models.RegisterSchemaV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/schema", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        

        r = self.client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.RegisterSchemaV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            pass
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.RegisterSchemaV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.RegisterSchemaV1Responses(raw_response=r.content)

        return res

    
    def upsert_api_endpoint_v1(self, request: models.UpsertAPIEndpointV1Request) -> models.UpsertAPIEndpointV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        

        r = self.client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.UpsertAPIEndpointV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.APIEndpoint])
                res.responses[r.status_code][mime_type] = models.UpsertAPIEndpointV1Responses(api_endpoint=out)
            else:
                res.responses[r.status_code][mime_type] = models.UpsertAPIEndpointV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.UpsertAPIEndpointV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.UpsertAPIEndpointV1Responses(raw_response=r.content)

        return res

    
    def upsert_api_v1(self, request: models.UpsertAPIV1Request) -> models.UpsertAPIV1Response:
        warnings.simplefilter("ignore")
        url = utils.generate_url(SERVER_URL, "/v1/apis/{apiID}", request.path_params)
        
        req_content_type, data, form = utils.serialize_request_body(request)
        headers = {}
        if req_content_type != "multipart/form-data":
            headers = {"content-type": req_content_type}
        if data is None and form is None:
           raise Exception('request body is required')
        

        r = self.client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "":
            mime_type = "unknown"

        res = models.UpsertAPIV1Response(status_code=r.status_code, content_type=mime_type, responses={r.status_code: {mime_type: {}}})
        if r.status_code == 200:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.API])
                res.responses[r.status_code][mime_type] = models.UpsertAPIV1Responses(api=out)
            else:
                res.responses[r.status_code][mime_type] = models.UpsertAPIV1Responses(raw_response=r.content)
        else:
            if mime_type == "application/json":
                out = utils.unmarshal_json(r.text, Optional[models.Error])
                res.responses[r.status_code][mime_type] = models.UpsertAPIV1Responses(error=out)
            else:
                res.responses[r.status_code][mime_type] = models.UpsertAPIV1Responses(raw_response=r.content)

        return res

    