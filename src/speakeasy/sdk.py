__doc__ = """ SDK Documentation: The Speakeasy API allows teams to manage common operations with their APIs
https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
import requests as requests_http
from . import utils
from .apiendpoints import APIEndpoints
from .apis import Apis
from .embeds import Embeds
from .metadata import Metadata
from .plugins import Plugins
from .requests import Requests
from .schemas import Schemas
from speakeasy.models import operations, shared
from typing import Optional

SERVER_PROD = "prod"
SERVERS = {
	SERVER_PROD: "https://api.prod.speakeasyapi.dev",
}

class Speakeasy:
    r"""SDK Documentation: The Speakeasy API allows teams to manage common operations with their APIs
    https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
    api_endpoints: APIEndpoints
    apis: Apis
    embeds: Embeds
    metadata: Metadata
    plugins: Plugins
    requests: Requests
    schemas: Schemas
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[SERVER_PROD]
    _language: str = "python"
    _sdk_version: str = "1.10.0"
    _gen_version: str = "1.11.0"

    def __init__(self,
                 security: shared.Security = None,
                 server: str = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server is not None:
            server_url = SERVERS[server]
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.api_endpoints = APIEndpoints(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apis = Apis(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.embeds = Embeds(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.metadata = Metadata(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.plugins = Plugins(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.requests = Requests(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.schemas = Schemas(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    def validate_api_key(self) -> operations.ValidateAPIKeyResponse:
        r"""Validate the current api key.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/auth/validate'
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ValidateAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    