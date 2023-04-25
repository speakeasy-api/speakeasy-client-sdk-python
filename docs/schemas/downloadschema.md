# download_schema
Available in: `schemas`

Download the latest schema for a particular apiID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSchemaRequest(
    api_id="cum",
    version_id="perferendis",
)

res = s.schemas.download_schema(req)

if res.schema is not None:
    # handle response
```