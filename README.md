# speakeasy-client-sdk-python

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install speakeasy-client-sdk-python
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetApisRequest(
    metadata={
        "provident": [
            'quibusdam',
            'unde',
            'nulla',
        ],
        "corrupti": [
            'vel',
            'error',
            'deserunt',
            'suscipit',
        ],
        "iure": [
            'debitis',
            'ipsa',
        ],
    },
    op=operations.GetApisOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [Speakeasy SDK](docs/speakeasy/README.md)

* [validate_api_key](docs/speakeasy/README.md#validate_api_key) - Validate the current api key.

### [api_endpoints](docs/apiendpoints/README.md)

* [delete_api_endpoint](docs/apiendpoints/README.md#delete_api_endpoint) - Delete an ApiEndpoint.
* [find_api_endpoint](docs/apiendpoints/README.md#find_api_endpoint) - Find an ApiEndpoint via its displayName.
* [generate_open_api_spec_for_api_endpoint](docs/apiendpoints/README.md#generate_open_api_spec_for_api_endpoint) - Generate an OpenAPI specification for a particular ApiEndpoint.
* [generate_postman_collection_for_api_endpoint](docs/apiendpoints/README.md#generate_postman_collection_for_api_endpoint) - Generate a Postman collection for a particular ApiEndpoint.
* [get_all_api_endpoints](docs/apiendpoints/README.md#get_all_api_endpoints) - Get all Api endpoints for a particular apiID.
* [get_all_for_version_api_endpoints](docs/apiendpoints/README.md#get_all_for_version_api_endpoints) - Get all ApiEndpoints for a particular apiID and versionID.
* [get_api_endpoint](docs/apiendpoints/README.md#get_api_endpoint) - Get an ApiEndpoint.
* [upsert_api_endpoint](docs/apiendpoints/README.md#upsert_api_endpoint) - Upsert an ApiEndpoint.

### [apis](docs/apis/README.md)

* [delete_api](docs/apis/README.md#delete_api) - Delete an Api.
* [generate_open_api_spec](docs/apis/README.md#generate_open_api_spec) - Generate an OpenAPI specification for a particular Api.
* [generate_postman_collection](docs/apis/README.md#generate_postman_collection) - Generate a Postman collection for a particular Api.
* [get_all_api_versions](docs/apis/README.md#get_all_api_versions) - Get all Api versions for a particular ApiEndpoint.
* [get_apis](docs/apis/README.md#get_apis) - Get a list of Apis for a given workspace
* [upsert_api](docs/apis/README.md#upsert_api) - Upsert an Api

### [embeds](docs/embeds/README.md)

* [get_embed_access_token](docs/embeds/README.md#get_embed_access_token) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](docs/embeds/README.md#get_valid_embed_access_tokens) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](docs/embeds/README.md#revoke_embed_access_token) - Revoke an embed access EmbedToken.

### [metadata](docs/metadata/README.md)

* [delete_version_metadata](docs/metadata/README.md#delete_version_metadata) - Delete metadata for a particular apiID and versionID.
* [get_version_metadata](docs/metadata/README.md#get_version_metadata) - Get all metadata for a particular apiID and versionID.
* [insert_version_metadata](docs/metadata/README.md#insert_version_metadata) - Insert metadata for a particular apiID and versionID.

### [plugins](docs/plugins/README.md)

* [get_plugins](docs/plugins/README.md#get_plugins) - Get all plugins for the current workspace.
* [run_plugin](docs/plugins/README.md#run_plugin) - Run a plugin
* [upsert_plugin](docs/plugins/README.md#upsert_plugin) - Upsert a plugin

### [requests](docs/requests/README.md)

* [generate_request_postman_collection](docs/requests/README.md#generate_request_postman_collection) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](docs/requests/README.md#get_request_from_event_log) - Get information about a particular request.
* [query_event_log](docs/requests/README.md#query_event_log) - Query the event log to retrieve a list of requests.

### [schemas](docs/schemas/README.md)

* [delete_schema](docs/schemas/README.md#delete_schema) - Delete a particular schema revision for an Api.
* [download_schema](docs/schemas/README.md#download_schema) - Download the latest schema for a particular apiID.
* [download_schema_revision](docs/schemas/README.md#download_schema_revision) - Download a particular schema revision for an Api.
* [get_schema](docs/schemas/README.md#get_schema) - Get information about the latest schema.
* [get_schema_diff](docs/schemas/README.md#get_schema_diff) - Get a diff of two schema revisions for an Api.
* [get_schema_revision](docs/schemas/README.md#get_schema_revision) - Get information about a particular schema revision for an Api.
* [get_schemas](docs/schemas/README.md#get_schemas) - Get information about all schemas associated with a particular apiID.
* [register_schema](docs/schemas/README.md#register_schema) - Register a schema.
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
