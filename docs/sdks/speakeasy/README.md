# Speakeasy SDK


## Overview

Speakeasy API: The Speakeasy API allows teams to manage common operations with their APIs

The Speakeasy Platform Documentation
</docs>
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
)


res = s.validate_api_key()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.ValidateAPIKeyResponse](../../models/operations/validateapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
