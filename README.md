# speakeasy-client-sdk-python

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install speakeasy-client-sdk-python
```

Poetry
```bash
poetry add speakeasy-client-sdk-python
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.get_apis()

if res.apis is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

async def main():
    s = Speakeasy(
        security=shared.Security(
            api_key=os.getenv("API_KEY", ""),
        ),
    )
    res = await s.apis.get_apis_async()
    if res.apis is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [apis](docs/sdks/apis/README.md)

* [delete_api](docs/sdks/apis/README.md#delete_api) - Delete an Api.
* [generate_open_api_spec](docs/sdks/apis/README.md#generate_open_api_spec) - Generate an OpenAPI specification for a particular Api.
* [generate_postman_collection](docs/sdks/apis/README.md#generate_postman_collection) - Generate a Postman collection for a particular Api.
* [get_all_api_versions](docs/sdks/apis/README.md#get_all_api_versions) - Get all Api versions for a particular ApiEndpoint.
* [get_apis](docs/sdks/apis/README.md#get_apis) - Get a list of Apis for a given workspace
* [upsert_api](docs/sdks/apis/README.md#upsert_api) - Upsert an Api

### [api_endpoints](docs/sdks/apiendpoints/README.md)

* [delete_api_endpoint](docs/sdks/apiendpoints/README.md#delete_api_endpoint) - Delete an ApiEndpoint.
* [find_api_endpoint](docs/sdks/apiendpoints/README.md#find_api_endpoint) - Find an ApiEndpoint via its displayName.
* [generate_open_api_spec_for_api_endpoint](docs/sdks/apiendpoints/README.md#generate_open_api_spec_for_api_endpoint) - Generate an OpenAPI specification for a particular ApiEndpoint.
* [generate_postman_collection_for_api_endpoint](docs/sdks/apiendpoints/README.md#generate_postman_collection_for_api_endpoint) - Generate a Postman collection for a particular ApiEndpoint.
* [get_all_api_endpoints](docs/sdks/apiendpoints/README.md#get_all_api_endpoints) - Get all Api endpoints for a particular apiID.
* [get_all_for_version_api_endpoints](docs/sdks/apiendpoints/README.md#get_all_for_version_api_endpoints) - Get all ApiEndpoints for a particular apiID and versionID.
* [get_api_endpoint](docs/sdks/apiendpoints/README.md#get_api_endpoint) - Get an ApiEndpoint.
* [upsert_api_endpoint](docs/sdks/apiendpoints/README.md#upsert_api_endpoint) - Upsert an ApiEndpoint.

### [metadata](docs/sdks/metadata/README.md)

* [delete_version_metadata](docs/sdks/metadata/README.md#delete_version_metadata) - Delete metadata for a particular apiID and versionID.
* [get_version_metadata](docs/sdks/metadata/README.md#get_version_metadata) - Get all metadata for a particular apiID and versionID.
* [insert_version_metadata](docs/sdks/metadata/README.md#insert_version_metadata) - Insert metadata for a particular apiID and versionID.

### [schemas](docs/sdks/schemas/README.md)

* [delete_schema](docs/sdks/schemas/README.md#delete_schema) - Delete a particular schema revision for an Api.
* [download_schema](docs/sdks/schemas/README.md#download_schema) - Download the latest schema for a particular apiID.
* [download_schema_revision](docs/sdks/schemas/README.md#download_schema_revision) - Download a particular schema revision for an Api.
* [get_schema](docs/sdks/schemas/README.md#get_schema) - Get information about the latest schema.
* [get_schema_diff](docs/sdks/schemas/README.md#get_schema_diff) - Get a diff of two schema revisions for an Api.
* [get_schema_revision](docs/sdks/schemas/README.md#get_schema_revision) - Get information about a particular schema revision for an Api.
* [get_schemas](docs/sdks/schemas/README.md#get_schemas) - Get information about all schemas associated with a particular apiID.
* [register_schema](docs/sdks/schemas/README.md#register_schema) - Register a schema.

### [artifacts](docs/sdks/artifacts/README.md)

* [get_blob](docs/sdks/artifacts/README.md#get_blob) - Get blob for a particular digest
* [get_manifest](docs/sdks/artifacts/README.md#get_manifest) - Get manifest for a particular reference
* [get_namespaces](docs/sdks/artifacts/README.md#get_namespaces) - Each namespace contains many revisions.
* [get_oas_summary](docs/sdks/artifacts/README.md#get_oas_summary)
* [get_revisions](docs/sdks/artifacts/README.md#get_revisions)
* [get_tags](docs/sdks/artifacts/README.md#get_tags)
* [post_tags](docs/sdks/artifacts/README.md#post_tags) - Add tags to an existing revision
* [preflight](docs/sdks/artifacts/README.md#preflight) - Get access token for communicating with OCI distribution endpoints

### [auth](docs/sdks/auth/README.md)

* [get_access_token](docs/sdks/auth/README.md#get_access_token) - Get or refresh an access token for the current workspace.
* [get_user](docs/sdks/auth/README.md#get_user) - Get information about the current user.
* [get_workspace_access](docs/sdks/auth/README.md#get_workspace_access) - Get access allowances for a particular workspace
* [validate_api_key](docs/sdks/auth/README.md#validate_api_key) - Validate the current api key.

### [requests](docs/sdks/requests/README.md)

* [generate_request_postman_collection](docs/sdks/requests/README.md#generate_request_postman_collection) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](docs/sdks/requests/README.md#get_request_from_event_log) - Get information about a particular request.
* [query_event_log](docs/sdks/requests/README.md#query_event_log) - Query the event log to retrieve a list of requests.

### [github](docs/sdks/github/README.md)

* [check_access](docs/sdks/github/README.md#check_access)
* [configure_code_samples](docs/sdks/github/README.md#configure_code_samples)
* [configure_mintlify_repo](docs/sdks/github/README.md#configure_mintlify_repo)
* [configure_target](docs/sdks/github/README.md#configure_target)
* [fetch_publishing_p_rs](docs/sdks/github/README.md#fetch_publishing_p_rs)
* [get_action](docs/sdks/github/README.md#get_action)
* [github_check_publishing_secrets](docs/sdks/github/README.md#github_check_publishing_secrets)
* [github_store_publishing_secrets](docs/sdks/github/README.md#github_store_publishing_secrets)
* [trigger_action](docs/sdks/github/README.md#trigger_action)

### [organizations](docs/sdks/organizations/README.md)

* [create_free_trial](docs/sdks/organizations/README.md#create_free_trial) - Create a free trial for an organization
* [get_organization](docs/sdks/organizations/README.md#get_organization) - Get organization
* [get_organization_usage](docs/sdks/organizations/README.md#get_organization_usage) - Get billing usage summary for a particular organization
* [get_organizations](docs/sdks/organizations/README.md#get_organizations) - Get organizations for a user

### [reports](docs/sdks/reports/README.md)

* [get_changes_report_signed_url](docs/sdks/reports/README.md#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.
* [get_linting_report_signed_url](docs/sdks/reports/README.md#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [upload_report](docs/sdks/reports/README.md#upload_report) - Upload a report.

### [short_ur_ls](docs/sdks/shorturls/README.md)

* [create](docs/sdks/shorturls/README.md#create) - Shorten a URL.

### [suggest](docs/sdks/suggest/README.md)

* [apply_operation_i_ds](docs/sdks/suggest/README.md#apply_operation_i_ds) - Apply operation ID suggestions and download result.
* [suggest_operation_i_ds](docs/sdks/suggest/README.md#suggest_operation_i_ds) - Generate operation ID suggestions.
* [suggest_operation_i_ds_registry](docs/sdks/suggest/README.md#suggest_operation_i_ds_registry) - Generate operation ID suggestions.

### [embeds](docs/sdks/embeds/README.md)

* [get_embed_access_token](docs/sdks/embeds/README.md#get_embed_access_token) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](docs/sdks/embeds/README.md#get_valid_embed_access_tokens) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](docs/sdks/embeds/README.md#revoke_embed_access_token) - Revoke an embed access EmbedToken.

### [workspaces](docs/sdks/workspaces/README.md)

* [get_workspace](docs/sdks/workspaces/README.md#get_workspace) - Get workspace

### [events](docs/sdks/events/README.md)

* [get_workspace_events_by_target](docs/sdks/events/README.md#get_workspace_events_by_target) - Load recent events for a particular workspace
* [get_workspace_targets](docs/sdks/events/README.md#get_workspace_targets) - Load targets for a particular workspace
* [post_workspace_events](docs/sdks/events/README.md#post_workspace_events) - Post events for a specific workspace
* [search_workspace_events](docs/sdks/events/README.md#search_workspace_events) - Search events for a particular workspace by any field
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import errors, shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)

res = None
try:
    res = s.events.get_workspace_events_by_target(request={
    "target_id": "<value>",
})

except errors.Error as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.cli_event_batch is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `prod` | `https://api.prod.speakeasyapi.dev` | None |

#### Example

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    server="prod",
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.delete_api(request={
    "api_id": "<value>",
    "version_id": "<value>",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    server_url="https://api.prod.speakeasyapi.dev",
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.delete_api(request={
    "api_id": "<value>",
    "version_id": "<value>",
})

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from speakeasy_client_sdk_python import Speakeasy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Speakeasy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Speakeasy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `api_key`   | apiKey      | API key     |
| `bearer`    | http        | HTTP Bearer |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.delete_api(request={
    "api_id": "<value>",
    "version_id": "<value>",
})

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `workspaceID` to `"<value>"` at SDK initialization and then you do not have to pass the same value on calls to operations like `get_workspace`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.

| Name | Type | Required | Description |
| ---- | ---- |:--------:| ----------- |
| workspace_id | str |  | The workspace_id parameter. |


### Example

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.workspaces.get_workspace()

if res.workspace is not None:
    # handle response
    pass

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from speakeasy.utils import BackoffStrategy, RetryConfig
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.delete_api(request={
    "api_id": "<value>",
    "version_id": "<value>",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from speakeasy.utils import BackoffStrategy, RetryConfig
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.apis.delete_api(request={
    "api_id": "<value>",
    "version_id": "<value>",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.schemas.register_schema(request={
    "api_id": "<value>",
    "version_id": "<value>",
    "request_body": {
        "file": {
            "content": open("<file_path>", "rb"),
            "file_name": "your_file_here",
        },
    },
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from speakeasy_client_sdk_python import Speakeasy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Speakeasy(debug_logger=logging.getLogger("speakeasy_client_sdk_python"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
