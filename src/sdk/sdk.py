__doc__ = """ SDK Documentation: https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
import requests
from . import utils
from .apiendpoints import APIEndpoints
from .apis import Apis
from .embeds import Embeds
from .metadata import Metadata
from .plugins import Plugins
from .requests import Requests
from .schemas import Schemas
from sdk.models import operations, shared
from typing import Optional

SERVER_PROD = "prod"
SERVERS = {
	SERVER_PROD: "https://api.prod.speakeasyapi.dev",
}


class SDK:
    r"""SDK Documentation: https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
    api_endpoints: APIEndpoints
    apis: Apis
    embeds: Embeds
    metadata: Metadata
    plugins: Plugins
    requests: Requests
    schemas: Schemas

    _client: requests.Session
    _security_client: requests.Session
    _security: shared.Security
    _server_url: str = SERVERS[SERVER_PROD]
    _language: str = "python"
    _sdk_version: str = "1.1.1"
    _gen_version: str = "1.1.2"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        self._init_sdks()


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if params is not None:
            self._server_url = utils.replace_parameters(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    def config_server(self, server: str, params: dict[str, str]):
        if not server in SERVERS:
            raise ValueError("Invalid server")
        self.config_server_url(SERVERS[server], params)
        self._init_sdks()
    

    def config_client(self, client: requests.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    

    def config_security(self, security: shared.Security):
        self._security = security
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
        
        url = base_url.removesuffix("/") + "/v1/auth/validate"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ValidateAPIKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out

        return res

    