"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from speakeasy_client_sdk_python import utils
from speakeasy_client_sdk_python._hooks import HookContext
from speakeasy_client_sdk_python.models import errors, operations, shared
from speakeasy_client_sdk_python.types import BaseModel, OptionalNullable, UNSET
from typing import Optional, Union, cast

class ApplyOperationIDsAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_X_YAML = "application/x-yaml"

class Suggest(BaseSDK):
    r"""REST APIs for managing LLM OAS suggestions"""
    
    
    def apply_operation_i_ds(
        self, *,
        request: Union[operations.ApplyOperationIDsRequest, operations.ApplyOperationIDsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ApplyOperationIDsAcceptEnum] = None
    ) -> operations.ApplyOperationIDsResponse:
        r"""Apply operation ID suggestions and download result.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.ApplyOperationIDsRequest)
        request = cast(operations.ApplyOperationIDsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids/apply",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value if accept_header_override is not None else "application/json;q=1, application/x-yaml;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[operations.ApplyOperationIDsRequestBody]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="applyOperationIDs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            stream=True,
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.ApplyOperationIDsResponse(two_hundred_application_json_schema=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return operations.ApplyOperationIDsResponse(two_hundred_application_x_yaml_schema=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.ApplyOperationIDsResponse(error=utils.unmarshal_json(utils.stream_to_text(http_res), Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def apply_operation_i_ds_async(
        self, *,
        request: Union[operations.ApplyOperationIDsRequest, operations.ApplyOperationIDsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[ApplyOperationIDsAcceptEnum] = None
    ) -> operations.ApplyOperationIDsResponse:
        r"""Apply operation ID suggestions and download result.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.ApplyOperationIDsRequest)
        request = cast(operations.ApplyOperationIDsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids/apply",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value if accept_header_override is not None else "application/json;q=1, application/x-yaml;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[operations.ApplyOperationIDsRequestBody]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="applyOperationIDs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            stream=True,
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.ApplyOperationIDsResponse(two_hundred_application_json_schema=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return operations.ApplyOperationIDsResponse(two_hundred_application_x_yaml_schema=http_res, status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        if utils.match_response(http_res, "default", "application/json"):
            return operations.ApplyOperationIDsResponse(error=utils.unmarshal_json(utils.stream_to_text(http_res), Optional[errors.Error]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def suggest_operation_i_ds(
        self, *,
        request: Union[operations.SuggestOperationIDsRequest, operations.SuggestOperationIDsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.SuggestOperationIDsResponse:
        r"""Generate operation ID suggestions.

        Get suggestions from an LLM model for improving the operationIDs in the provided schema.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SuggestOperationIDsRequest)
        request = cast(operations.SuggestOperationIDsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "multipart", operations.SuggestOperationIDsRequestBody),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="suggestOperationIDs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.SuggestOperationIDsResponse(suggested_operation_i_ds=utils.unmarshal_json(http_res.text, Optional[shared.SuggestedOperationIDs]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def suggest_operation_i_ds_async(
        self, *,
        request: Union[operations.SuggestOperationIDsRequest, operations.SuggestOperationIDsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.SuggestOperationIDsResponse:
        r"""Generate operation ID suggestions.

        Get suggestions from an LLM model for improving the operationIDs in the provided schema.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SuggestOperationIDsRequest)
        request = cast(operations.SuggestOperationIDsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "multipart", operations.SuggestOperationIDsRequestBody),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="suggestOperationIDs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.SuggestOperationIDsResponse(suggested_operation_i_ds=utils.unmarshal_json(http_res.text, Optional[shared.SuggestedOperationIDs]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def suggest_operation_i_ds_registry(
        self, *,
        request: Union[operations.SuggestOperationIDsRegistryRequest, operations.SuggestOperationIDsRegistryRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.SuggestOperationIDsRegistryResponse:
        r"""Generate operation ID suggestions.

        Get suggestions from an LLM model for improving the operationIDs in the provided schema.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SuggestOperationIDsRegistryRequest)
        request = cast(operations.SuggestOperationIDsRegistryRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids/{namespace_name}/{revision_reference}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.suggest_operation_i_ds_opts, False, True, "json", Optional[shared.SuggestOperationIDsOpts]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="suggestOperationIDsRegistry", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.SuggestOperationIDsRegistryResponse(suggested_operation_i_ds=utils.unmarshal_json(http_res.text, Optional[shared.SuggestedOperationIDs]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def suggest_operation_i_ds_registry_async(
        self, *,
        request: Union[operations.SuggestOperationIDsRegistryRequest, operations.SuggestOperationIDsRegistryRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.SuggestOperationIDsRegistryResponse:
        r"""Generate operation ID suggestions.

        Get suggestions from an LLM model for improving the operationIDs in the provided schema.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.SuggestOperationIDsRegistryRequest)
        request = cast(operations.SuggestOperationIDsRegistryRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/suggest/operation_ids/{namespace_name}/{revision_reference}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.suggest_operation_i_ds_opts, False, True, "json", Optional[shared.SuggestOperationIDsOpts]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="suggestOperationIDsRegistry", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.SuggestOperationIDsRegistryResponse(suggested_operation_i_ds=utils.unmarshal_json(http_res.text, Optional[shared.SuggestedOperationIDs]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
