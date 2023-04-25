# get_plugins
Available in: `plugins`

Get all plugins for the current workspace.

## Example Usage
```python
import speakeasy


s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


res = s.plugins.get_plugins()

if res.plugins is not None:
    # handle response
```