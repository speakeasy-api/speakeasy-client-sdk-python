# Artifacts
(*artifacts*)

### Available Operations

* [get_namespaces](#get_namespaces) - Each namespace contains many revisions.
* [get_revisions](#get_revisions)
* [preflight](#preflight) - Get access token for communicating with OCI distribution endpoints

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
    namespace_id='<value>',
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


res = s.artifacts.preflight()

if res.preflight_token is not None:
    # handle response
    pass

```


### Response

**[operations.PreflightResponse](../../models/operations/preflightresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
