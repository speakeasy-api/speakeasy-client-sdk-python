
__doc__ = """ SDK Documentation: https://docs.speakeasyapi.dev - The Speakeasy Platform Documentation"""
import requests
from sdk.models import shared
from . import utils

from .apiendpoints import APIEndpoints
from .apis import Apis
from .embeds import Embeds
from .metadata import Metadata
from .requests import Requests
from .schemas import Schemas


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
    requests: Requests
    schemas: Schemas

    _client: requests.Session
    _security_client: requests.Session
    _security: shared.Security
    _server_url: str = SERVERS[SERVER_PROD]
    _language: str = "python"
    _sdk_version: str = "0.8.0"
    _gen_version: str = "0.16.0"

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
    
    