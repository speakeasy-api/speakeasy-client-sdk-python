"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from speakeasy.models import shared
from typing import Any, Callable, Dict, Tuple, Union


SERVER_PROD = 'prod'
SERVERS = {
	SERVER_PROD: 'https://api.prod.speakeasyapi.dev',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server: str = ''
    globals: Dict[str, Dict[str, Dict[str, Any]]] = field(default_factory=Dict)
    language: str = 'python'
    openapi_doc_version: str = '0.4.0'
    sdk_version: str = '5.2.7'
    gen_version: str = '2.272.7'
    user_agent: str = 'speakeasy-sdk/python 5.2.7 2.272.7 0.4.0 speakeasy-client-sdk-python'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], {}
