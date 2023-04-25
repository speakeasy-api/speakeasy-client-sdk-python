# download_schema_revision
Available in: `schemas`

Download a particular schema revision for an Api.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSchemaRevisionRequest(
    api_id="doloremque",
    revision_id="reprehenderit",
    version_id="ut",
)

res = s.schemas.download_schema_revision(req)

if res.schema is not None:
    # handle response
```