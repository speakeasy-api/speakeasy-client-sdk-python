"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from speakeasy.models import internal, shared
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_PROD = 'prod'
SERVERS = {
	SERVER_PROD: 'https://api.prod.speakeasyapi.dev',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    globals: internal.Globals
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: Optional[str] = ''
    server: Optional[str] = ''
    language: str = 'python'
    openapi_doc_version: str = '0.4.0 .'
    sdk_version: str = '5.9.16'
    gen_version: str = '2.342.6'
    user_agent: str = 'speakeasy-sdk/python 5.9.16 2.342.6 0.4.0 . speakeasy-client-sdk-python'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        if self.server not in SERVERS:
            raise ValueError(f"Invalid server \"{self.server}\"")

        return SERVERS[self.server], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
