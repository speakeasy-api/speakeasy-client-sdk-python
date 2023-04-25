# get_all_for_version_api_endpoints
Available in: `api_endpoints`

Get all ApiEndpoints for a particular apiID and versionID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllForVersionAPIEndpointsRequest(
    api_id="quis",
    version_id="veritatis",
)

res = s.api_endpoints.get_all_for_version_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```