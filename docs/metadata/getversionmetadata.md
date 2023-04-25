# get_version_metadata
Available in: `metadata`

Get all metadata for a particular apiID and versionID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetVersionMetadataRequest(
    api_id="doloribus",
    version_id="sapiente",
)

res = s.metadata.get_version_metadata(req)

if res.version_metadata is not None:
    # handle response
```