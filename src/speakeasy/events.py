"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from speakeasy import utils
from speakeasy.models import errors, operations
from typing import Optional

class Events:
    r"""REST APIs for capturing event data"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def post_workspace_events(self, request: operations.PostWorkspaceEventsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.PostWorkspaceEventsResponse:
        r"""Post events for a specific workspace
        Sends an array of events to be stored for a particular workspace.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostWorkspaceEventsRequest, base_url, '/v1/workspace/{workspaceID}/events', request, self.sdk_configuration.globals)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.PostWorkspaceEventsRequest, "request_body", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(100, 2000, 1.5, 30000), True)

        def do_request():
            return client.request('POST', url, data=data, files=form, headers=headers)

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '500',
            '502',
            '503'
        ]))
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostWorkspaceEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code >= 200 and http_res.status_code < 300:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 500 and http_res.status_code < 600:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Error)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    