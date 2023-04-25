# get_apis
Available in: `apis`

Get a list of all Apis and their versions for a given workspace.
Supports filtering the APIs based on metadata attributes.

## Example Usage
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
        "esse": [
            "excepturi",
        ],
        "aspernatur": [
            "ad",
        ],
        "natus": [
            "iste",
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