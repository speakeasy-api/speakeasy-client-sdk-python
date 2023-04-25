# insert_version_metadata
Available in: `metadata`

Insert metadata for a particular apiID and versionID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.InsertVersionMetadataRequest(
    version_metadata_input=shared.VersionMetadataInput(
        meta_key="architecto",
        meta_value="mollitia",
    ),
    api_id="dolorem",
    version_id="culpa",
)

res = s.metadata.insert_version_metadata(req)

if res.version_metadata is not None:
    # handle response
```