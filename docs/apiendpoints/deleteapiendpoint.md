# delete_api_endpoint
Available in: `api_endpoints`

Delete an ApiEndpoint. This will also delete all associated Request Logs (if using a Postgres datastore).

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteAPIEndpointRequest(
    api_endpoint_id="delectus",
    api_id="tempora",
    version_id="suscipit",
)

res = s.api_endpoints.delete_api_endpoint(req)

if res.status_code == 200:
    # handle response
```