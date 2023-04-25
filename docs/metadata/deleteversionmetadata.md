# delete_version_metadata
Available in: `metadata`

Delete metadata for a particular apiID and versionID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteVersionMetadataRequest(
    api_id="excepturi",
    meta_key="accusantium",
    meta_value="iure",
    version_id="culpa",
)

res = s.metadata.delete_version_metadata(req)

if res.status_code == 200:
    # handle response
```