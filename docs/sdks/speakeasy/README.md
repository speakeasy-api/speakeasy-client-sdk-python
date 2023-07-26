# Speakeasy SDK

## Overview

Speakeasy API: The Speakeasy API allows teams to manage common operations with their APIs

The Speakeasy Platform Documentation
<https://speakeasyapi.dev/docs/>
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
        api_key="",
    ),
)


res = s.speakeasy.validate_api_key()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.ValidateAPIKeyResponse](../../models/operations/validateapikeyresponse.md)**

