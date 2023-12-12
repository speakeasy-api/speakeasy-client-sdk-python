# speakeasy-client-sdk-python

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install speakeasy-client-sdk-python
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetApisRequest(
    metadata={
        'key': [
            'string',
        ],
    },
    op=operations.QueryParamOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.classes is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [Speakeasy SDK](docs/sdks/speakeasy/README.md)

* [validate_api_key](docs/sdks/speakeasy/README.md#validate_api_key) - Validate the current api key.

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

### [requests](docs/sdks/requests/README.md)

* [generate_request_postman_collection](docs/sdks/requests/README.md#generate_request_postman_collection) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](docs/sdks/requests/README.md#get_request_from_event_log) - Get information about a particular request.
* [query_event_log](docs/sdks/requests/README.md#query_event_log) - Query the event log to retrieve a list of requests.

### [plugins](docs/sdks/plugins/README.md)

* [get_plugins](docs/sdks/plugins/README.md#get_plugins) - Get all plugins for the current workspace.
* [run_plugin](docs/sdks/plugins/README.md#run_plugin) - Run a plugin
* [upsert_plugin](docs/sdks/plugins/README.md#upsert_plugin) - Upsert a plugin

### [embeds](docs/sdks/embeds/README.md)

* [get_embed_access_token](docs/sdks/embeds/README.md#get_embed_access_token) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](docs/sdks/embeds/README.md#get_valid_embed_access_tokens) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](docs/sdks/embeds/README.md#revoke_embed_access_token) - Revoke an embed access EmbedToken.
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = None
try:
    res = s.validate_api_key()
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.status_code == 200:
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
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    server="prod",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.validate_api_key()

if res.status_code == 200:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    server_url="https://api.prod.speakeasyapi.dev",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.validate_api_key()

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import speakeasy
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = speakeasy.Speakeasy(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.validate_api_key()

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
