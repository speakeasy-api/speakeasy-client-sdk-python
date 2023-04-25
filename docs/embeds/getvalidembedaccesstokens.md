# get_valid_embed_access_tokens
Available in: `embeds`

Get all valid embed access tokens for the current workspace.

## Example Usage
```python
import speakeasy


s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


res = s.embeds.get_valid_embed_access_tokens()

if res.embed_tokens is not None:
    # handle response
```