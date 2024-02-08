# Auth
(*auth*)

## Overview

REST APIs for managing Authentication

### Available Operations

* [validate_api_key](#validate_api_key) - Validate the current api key.

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
    workspace_id='string',
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
