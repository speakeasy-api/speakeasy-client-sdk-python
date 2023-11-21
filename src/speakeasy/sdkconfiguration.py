"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from speakeasy.models import shared


SERVER_PROD = 'prod'
SERVERS = {
	SERVER_PROD: 'https://api.prod.speakeasyapi.dev',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server: str = ''
    language: str = 'python'
    openapi_doc_version: str = '0.3.0'
    sdk_version: str = '3.1.3'
    gen_version: str = '2.195.2'
    user_agent: str = 'speakeasy-sdk/python 3.1.3 2.195.2 0.3.0 speakeasy-client-sdk-python'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], {}
