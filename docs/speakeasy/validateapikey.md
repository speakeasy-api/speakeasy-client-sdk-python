# validate_api_key
Available in: `speakeasy`

Validate the current api key.

## Example Usage
```python
import speakeasy


s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


res = s.speakeasy.validate_api_key()

if res.status_code == 200:
    # handle response
```