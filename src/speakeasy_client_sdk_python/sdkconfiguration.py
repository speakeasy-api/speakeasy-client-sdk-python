"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from dataclasses import dataclass
from pydantic import Field
from speakeasy_client_sdk_python.models import internal, shared
from speakeasy_client_sdk_python.types import OptionalNullable, UNSET
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_PROD = "prod"
SERVERS = {
    SERVER_PROD: "https://api.prod.speakeasyapi.dev",
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    globals: internal.Globals
    security: Optional[Union[shared.Security, Callable[[], shared.Security]]] = None
    server_url: Optional[str] = ""
    server: Optional[str] = ""
    language: str = "python"
    openapi_doc_version: str = "0.4.0"
    sdk_version: str = "7.0.0-rc.2"
    gen_version: str = "2.457.9"
    user_agent: str = (
        "speakeasy-sdk/python 7.0.0-rc.2 2.457.9 0.4.0 speakeasy-client-sdk-python"
    )
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if not self.server:
            self.server = SERVER_PROD

        if self.server not in SERVERS:
            raise ValueError(f'Invalid server "{self.server}"')

        return SERVERS[self.server], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks
