# upsert_plugin
Available in: `plugins`

Upsert a plugin

## Example Usage
```python
import speakeasy
import dateutil.parser
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = shared.Plugin(
    code="velit",
    created_at=dateutil.parser.isoparse('2022-09-06T22:51:09.401Z'),
    eval_hash="quis",
    plugin_id="vitae",
    title="Miss",
    updated_at=dateutil.parser.isoparse('2022-05-14T10:37:30.872Z'),
    workspace_id="odit",
)

res = s.plugins.upsert_plugin(req)

if res.plugin is not None:
    # handle response
```