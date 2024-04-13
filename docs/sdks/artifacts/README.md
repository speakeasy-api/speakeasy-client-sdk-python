# Artifacts
(*artifacts*)

### Available Operations

* [get_blob](#get_blob) - Get blob for a particular digest
* [get_manifest](#get_manifest) - Get manifest for a particular reference
* [get_namespaces](#get_namespaces) - Each namespace contains many revisions.
* [get_revisions](#get_revisions)
* [get_tags](#get_tags)
* [preflight](#preflight) - Get access token for communicating with OCI distribution endpoints

## get_blob

Get blob for a particular digest

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)

req = operations.GetBlobRequest(
    digest='<value>',
    namespace_name='<value>',
    organization_slug='<value>',
    workspace_slug='<value>',
)

res = s.artifacts.get_blob(req)

if res.blob is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetBlobRequest](../../models/operations/getblobrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetBlobResponse](../../models/operations/getblobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_manifest

Get manifest for a particular reference

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)

req = operations.GetManifestRequest(
    namespace_name='<value>',
    organization_slug='<value>',
    revision_reference='<value>',
    workspace_slug='<value>',
)

res = s.artifacts.get_manifest(req)

if res.manifest is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetManifestRequest](../../models/operations/getmanifestrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetManifestResponse](../../models/operations/getmanifestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_namespaces

Each namespace contains many revisions.

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)


res = s.artifacts.get_namespaces()

if res.get_namespaces_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetNamespacesResponse](../../models/operations/getnamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_revisions

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)

req = operations.GetRevisionsRequest(
    namespace_name='<value>',
)

res = s.artifacts.get_revisions(req)

if res.get_revisions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetRevisionsRequest](../../models/operations/getrevisionsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetRevisionsResponse](../../models/operations/getrevisionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_tags

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)

req = operations.GetTagsRequest(
    namespace_name='<value>',
)

res = s.artifacts.get_tags(req)

if res.get_tags_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTagsRequest](../../models/operations/gettagsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetTagsResponse](../../models/operations/gettagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## preflight

Get access token for communicating with OCI distribution endpoints

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='<value>',
)

req = shared.PreflightRequest(
    namespace_name='<value>',
)

res = s.artifacts.preflight(req)

if res.preflight_token is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.PreflightRequest](../../models/shared/preflightrequest.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PreflightResponse](../../models/operations/preflightresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
