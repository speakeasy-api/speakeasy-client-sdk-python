# run_plugin
Available in: `plugins`

Run a plugin

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RunPluginRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key="repellat",
                operator="mollitia",
                value="occaecati",
            ),
        ],
        limit=253291,
        offset=414369,
        operator="quam",
    ),
    plugin_id="molestiae",
)

res = s.plugins.run_plugin(req)

if res.bounded_requests is not None:
    # handle response
```