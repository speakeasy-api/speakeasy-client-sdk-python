# Auth
(*auth*)

## Overview

REST APIs for managing Authentication

### Available Operations

* [get_access_token](#get_access_token) - Get or refresh an access token for the current workspace.
* [get_workspace_access](#get_workspace_access) - Get access allowances for a particular workspace
* [validate_api_key](#validate_api_key) - Validate the current api key.

## get_access_token

Get or refresh an access token for the current workspace.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    workspace_id='<value>',
)

req = operations.GetAccessTokenRequest(
    workspace_id='<value>',
)

res = s.auth.get_access_token(req)

if res.access_token is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAccessTokenRequest](../../models/operations/getaccesstokenrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetAccessTokenResponse](../../models/operations/getaccesstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_workspace_access

Checks if generation is permitted for a particular run of the CLI

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

req = operations.GetWorkspaceAccessRequest()

res = s.auth.get_workspace_access(req)

if res.access_details is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetWorkspaceAccessRequest](../../models/operations/getworkspaceaccessrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.GetWorkspaceAccessResponse](../../models/operations/getworkspaceaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## validate_api_key

Validate the current api key.

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


res = s.auth.validate_api_key()

if res.api_key_details is not None:
    # handle response
    pass

```


### Response

**[operations.ValidateAPIKeyResponse](../../models/operations/validateapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
