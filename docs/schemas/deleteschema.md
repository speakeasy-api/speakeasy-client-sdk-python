# delete_schema
Available in: `schemas`

Delete a particular schema revision for an Api.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteSchemaRequest(
    api_id="ipsa",
    revision_id="omnis",
    version_id="voluptate",
)

res = s.schemas.delete_schema(req)

if res.status_code == 200:
    # handle response
```