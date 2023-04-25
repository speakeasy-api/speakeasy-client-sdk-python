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
            "quibusdam",
            "unde",
            "nulla",
        ],
        "corrupti": [
            "vel",
            "error",
            "deserunt",
            "suscipit",
        ],
        "iure": [
            "debitis",
            "ipsa",
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

* [validate_api_key](docs/speakeasy/validateapikey.md) - Validate the current api key.

### [api_endpoints](docs/apiendpoints/README.md)

* [delete_api_endpoint](docs/apiendpoints/deleteapiendpoint.md) - Delete an ApiEndpoint.
* [find_api_endpoint](docs/apiendpoints/findapiendpoint.md) - Find an ApiEndpoint via its displayName.
* [generate_open_api_spec_for_api_endpoint](docs/apiendpoints/generateopenapispecforapiendpoint.md) - Generate an OpenAPI specification for a particular ApiEndpoint.
* [generate_postman_collection_for_api_endpoint](docs/apiendpoints/generatepostmancollectionforapiendpoint.md) - Generate a Postman collection for a particular ApiEndpoint.
* [get_all_api_endpoints](docs/apiendpoints/getallapiendpoints.md) - Get all Api endpoints for a particular apiID.
* [get_all_for_version_api_endpoints](docs/apiendpoints/getallforversionapiendpoints.md) - Get all ApiEndpoints for a particular apiID and versionID.
* [get_api_endpoint](docs/apiendpoints/getapiendpoint.md) - Get an ApiEndpoint.
* [upsert_api_endpoint](docs/apiendpoints/upsertapiendpoint.md) - Upsert an ApiEndpoint.

### [apis](docs/apis/README.md)

* [delete_api](docs/apis/deleteapi.md) - Delete an Api.
* [generate_open_api_spec](docs/apis/generateopenapispec.md) - Generate an OpenAPI specification for a particular Api.
* [generate_postman_collection](docs/apis/generatepostmancollection.md) - Generate a Postman collection for a particular Api.
* [get_all_api_versions](docs/apis/getallapiversions.md) - Get all Api versions for a particular ApiEndpoint.
* [get_apis](docs/apis/getapis.md) - Get a list of Apis for a given workspace
* [upsert_api](docs/apis/upsertapi.md) - Upsert an Api

### [embeds](docs/embeds/README.md)

* [get_embed_access_token](docs/embeds/getembedaccesstoken.md) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](docs/embeds/getvalidembedaccesstokens.md) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](docs/embeds/revokeembedaccesstoken.md) - Revoke an embed access EmbedToken.

### [metadata](docs/metadata/README.md)

* [delete_version_metadata](docs/metadata/deleteversionmetadata.md) - Delete metadata for a particular apiID and versionID.
* [get_version_metadata](docs/metadata/getversionmetadata.md) - Get all metadata for a particular apiID and versionID.
* [insert_version_metadata](docs/metadata/insertversionmetadata.md) - Insert metadata for a particular apiID and versionID.

### [plugins](docs/plugins/README.md)

* [get_plugins](docs/plugins/getplugins.md) - Get all plugins for the current workspace.
* [run_plugin](docs/plugins/runplugin.md) - Run a plugin
* [upsert_plugin](docs/plugins/upsertplugin.md) - Upsert a plugin

### [requests](docs/requests/README.md)

* [generate_request_postman_collection](docs/requests/generaterequestpostmancollection.md) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](docs/requests/getrequestfromeventlog.md) - Get information about a particular request.
* [query_event_log](docs/requests/queryeventlog.md) - Query the event log to retrieve a list of requests.

### [schemas](docs/schemas/README.md)

* [delete_schema](docs/schemas/deleteschema.md) - Delete a particular schema revision for an Api.
* [download_schema](docs/schemas/downloadschema.md) - Download the latest schema for a particular apiID.
* [download_schema_revision](docs/schemas/downloadschemarevision.md) - Download a particular schema revision for an Api.
* [get_schema](docs/schemas/getschema.md) - Get information about the latest schema.
* [get_schema_diff](docs/schemas/getschemadiff.md) - Get a diff of two schema revisions for an Api.
* [get_schema_revision](docs/schemas/getschemarevision.md) - Get information about a particular schema revision for an Api.
* [get_schemas](docs/schemas/getschemas.md) - Get information about all schemas associated with a particular apiID.
* [register_schema](docs/schemas/registerschema.md) - Register a schema.
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
