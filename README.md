undefined
<!-- Start Summary [summary] -->
## Summary

Speakeasy API: The Subscriptions API manages subscriptions for CLI and registry events

For more information about the API: [The Speakeasy Platform Documentation](/docs)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Global Parameters](#global-parameters)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install speakeasy-client-sdk-python
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add speakeasy-client-sdk-python
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from speakeasy-client-sdk-python python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "speakeasy-client-sdk-python",
# ]
# ///

from speakeasy_client_sdk_python import Speakeasy

sdk = Speakeasy(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

async def main():
    async with Speakeasy(
        security=shared.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as speakeasy:

        res = await speakeasy.artifacts.create_remote_source_async()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                   | Type   | Scheme      |
| ---------------------- | ------ | ----------- |
| `api_key`              | apiKey | API key     |
| `bearer`               | http   | HTTP Bearer |
| `workspace_identifier` | apiKey | API key     |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [artifacts](docs/sdks/artifacts/README.md)

* [create_remote_source](docs/sdks/artifacts/README.md#create_remote_source) - Configure a new remote source
* [get_blob](docs/sdks/artifacts/README.md#get_blob) - Get blob for a particular digest
* [get_manifest](docs/sdks/artifacts/README.md#get_manifest) - Get manifest for a particular reference
* [get_namespaces](docs/sdks/artifacts/README.md#get_namespaces) - Each namespace contains many revisions.
* [get_revisions](docs/sdks/artifacts/README.md#get_revisions)
* [get_tags](docs/sdks/artifacts/README.md#get_tags)
* [list_remote_sources](docs/sdks/artifacts/README.md#list_remote_sources) - Get remote sources attached to a particular namespace
* [post_tags](docs/sdks/artifacts/README.md#post_tags) - Add tags to an existing revision
* [preflight](docs/sdks/artifacts/README.md#preflight) - Get access token for communicating with OCI distribution endpoints
* [set_archived](docs/sdks/artifacts/README.md#set_archived) - Set whether a namespace is archived
* [set_visibility](docs/sdks/artifacts/README.md#set_visibility) - Set visibility of a namespace with an existing metadata entry

### [auth](docs/sdks/auth/README.md)

* [get_access](docs/sdks/auth/README.md#get_access) - Get access allowances for a particular workspace
* [get_access_token](docs/sdks/auth/README.md#get_access_token) - Get or refresh an access token for the current workspace.
* [get_user](docs/sdks/auth/README.md#get_user) - Get information about the current user.
* [validate_api_key](docs/sdks/auth/README.md#validate_api_key) - Validate the current api key.

### [code_samples](docs/sdks/codesamples/README.md)

* [generate_code_sample_preview](docs/sdks/codesamples/README.md#generate_code_sample_preview) - Generate Code Sample previews from a file and configuration parameters.
* [generate_code_sample_preview_asynchronous](docs/sdks/codesamples/README.md#generate_code_sample_preview_asynchronous) - Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an async JobID response for polling.
* [get](docs/sdks/codesamples/README.md#get) - Retrieve usage snippets
* [get_code_sample_preview_async](docs/sdks/codesamples/README.md#get_code_sample_preview_async) - Poll for the result of an asynchronous Code Sample preview generation.

### [events](docs/sdks/events/README.md)

* [get_events_by_target](docs/sdks/events/README.md#get_events_by_target) - Load recent events for a particular workspace
* [get_targets](docs/sdks/events/README.md#get_targets) - Load targets for a particular workspace
* [get_targets_deprecated](docs/sdks/events/README.md#get_targets_deprecated) - Load targets for a particular workspace
* [post](docs/sdks/events/README.md#post) - Post events for a specific workspace
* [search](docs/sdks/events/README.md#search) - Search events for a particular workspace by any field

### [github](docs/sdks/github/README.md)

* [check_access](docs/sdks/github/README.md#check_access)
* [check_publishing_p_rs](docs/sdks/github/README.md#check_publishing_p_rs)
* [check_publishing_secrets](docs/sdks/github/README.md#check_publishing_secrets)
* [configure_code_samples](docs/sdks/github/README.md#configure_code_samples)
* [configure_mintlify_repo](docs/sdks/github/README.md#configure_mintlify_repo)
* [configure_target](docs/sdks/github/README.md#configure_target)
* [get_action](docs/sdks/github/README.md#get_action)
* [get_setup](docs/sdks/github/README.md#get_setup)
* [link_github](docs/sdks/github/README.md#link_github)
* [store_publishing_secrets](docs/sdks/github/README.md#store_publishing_secrets)
* [trigger_action](docs/sdks/github/README.md#trigger_action)

### [organizations](docs/sdks/organizations/README.md)

* [create](docs/sdks/organizations/README.md#create) - Create an organization
* [create_free_trial](docs/sdks/organizations/README.md#create_free_trial) - Create a free trial for an organization
* [get](docs/sdks/organizations/README.md#get) - Get organization
* [get_all](docs/sdks/organizations/README.md#get_all) - Get organizations for a user
* [get_usage](docs/sdks/organizations/README.md#get_usage) - Get billing usage summary for a particular organization

### [reports](docs/sdks/reports/README.md)

* [get_changes_report_signed_url](docs/sdks/reports/README.md#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.
* [get_linting_report_signed_url](docs/sdks/reports/README.md#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [upload_report](docs/sdks/reports/README.md#upload_report) - Upload a report.

### [short_ur_ls](docs/sdks/shorturls/README.md)

* [create](docs/sdks/shorturls/README.md#create) - Shorten a URL.


### [subscriptions](docs/sdks/subscriptions/README.md)

* [activate_subscription_namespace](docs/sdks/subscriptions/README.md#activate_subscription_namespace) - Activate an ignored namespace for a subscription
* [ignore_subscription_namespace](docs/sdks/subscriptions/README.md#ignore_subscription_namespace) - Ignored a namespace for a subscription

### [suggest](docs/sdks/suggest/README.md)

* [suggest](docs/sdks/suggest/README.md#suggest) - Generate suggestions for improving an OpenAPI document.
* [suggest_items](docs/sdks/suggest/README.md#suggest_items) - Generate generic suggestions for a list of items.
* [suggest_open_api](docs/sdks/suggest/README.md#suggest_open_api) - (DEPRECATED) Generate suggestions for improving an OpenAPI document.
* [suggest_open_api_registry](docs/sdks/suggest/README.md#suggest_open_api_registry) - Generate suggestions for improving an OpenAPI document stored in the registry.

### [workspaces](docs/sdks/workspaces/README.md)

* [create](docs/sdks/workspaces/README.md#create) - Create a workspace
* [create_token](docs/sdks/workspaces/README.md#create_token) - Create a token for a particular workspace
* [delete_token](docs/sdks/workspaces/README.md#delete_token) - Delete a token for a particular workspace
* [get](docs/sdks/workspaces/README.md#get) - Get workspace by context
* [get_all](docs/sdks/workspaces/README.md#get_all) - Get workspaces for a user
* [get_by_id](docs/sdks/workspaces/README.md#get_by_id) - Get workspace
* [get_feature_flags](docs/sdks/workspaces/README.md#get_feature_flags) - Get workspace feature flags
* [get_settings](docs/sdks/workspaces/README.md#get_settings) - Get workspace settings
* [get_team](docs/sdks/workspaces/README.md#get_team) - Get team members for a particular workspace
* [get_tokens](docs/sdks/workspaces/README.md#get_tokens) - Get tokens for a particular workspace
* [grant_access](docs/sdks/workspaces/README.md#grant_access) - Grant a user access to a particular workspace
* [revoke_access](docs/sdks/workspaces/README.md#revoke_access) - Revoke a user's access to a particular workspace
* [set_feature_flags](docs/sdks/workspaces/README.md#set_feature_flags) - Set workspace feature flags
* [update](docs/sdks/workspaces/README.md#update) - Update workspace details
* [update_settings](docs/sdks/workspaces/README.md#update_settings) - Update workspace settings

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `workspace_id` to `"<id>"` at SDK initialization and then you do not have to pass the same value on calls to operations like `get_access_token`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.

| Name         | Type | Description                 |
| ------------ | ---- | --------------------------- |
| workspace_id | str  | The workspace_id parameter. |

### Example

```python
from speakeasy_client_sdk_python import Speakeasy

with Speakeasy() as speakeasy:

    res = speakeasy.auth.get_access_token(request={
        "workspace_id": "<id>",
    })

    assert res.access_token is not None

    # Handle response
    print(res.access_token)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.code_samples.generate_code_sample_preview(request={
        "language": "<value>",
        "schema_file": {
            "content": open("example.file", "rb"),
            "file_name": "example.file",
        },
    })

    assert res.usage_snippets is not None

    # Handle response
    print(res.usage_snippets)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import BackoffStrategy, RetryConfig

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import BackoffStrategy, RetryConfig

with Speakeasy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_remote_source_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type     |
| --------------- | ----------- | ---------------- |
| errors.Error    | 4XX         | application/json |
| errors.SDKError | 5XX         | \*/\*            |

### Example

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import errors, shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:
    res = None
    try:

        res = speakeasy.artifacts.create_remote_source()

        assert res is not None

        # Handle response
        print(res)

    except errors.Error as e:
        # handle e.data: errors.ErrorData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name   | Server                              |
| ------ | ----------------------------------- |
| `prod` | `https://api.prod.speakeasyapi.dev` |

#### Example

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    server="prod",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    server_url="https://api.prod.speakeasyapi.dev",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)

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

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Speakeasy` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
def main():
    with Speakeasy(
        security=shared.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as speakeasy:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Speakeasy(
        security=shared.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as speakeasy:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from speakeasy_client_sdk_python import Speakeasy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Speakeasy(debug_logger=logging.getLogger("speakeasy_client_sdk_python"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
