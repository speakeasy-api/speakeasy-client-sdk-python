# get_all_api_versions
Available in: `apis`

Get all Api versions for a particular ApiEndpoint.
Supports filtering the versions based on metadata attributes.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllAPIVersionsRequest(
    api_id="nam",
    metadata={
        "occaecati": [
            "deleniti",
        ],
        "hic": [
            "totam",
            "beatae",
            "commodi",
            "molestiae",
        ],
        "modi": [
            "impedit",
        ],
    },
    op=operations.GetAllAPIVersionsOp(
        and_=False,
    ),
)

res = s.apis.get_all_api_versions(req)

if res.apis is not None:
    # handle response
```