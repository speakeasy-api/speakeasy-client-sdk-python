# delete_api
Available in: `apis`

Delete a particular version of an Api. The will also delete all associated ApiEndpoints, Metadata, Schemas & Request Logs (if using a Postgres datastore).

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteAPIRequest(
    api_id="quod",
    version_id="esse",
)

res = s.apis.delete_api(req)

if res.status_code == 200:
    # handle response
```