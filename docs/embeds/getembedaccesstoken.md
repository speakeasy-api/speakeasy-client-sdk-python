# get_embed_access_token
Available in: `embeds`

Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
Filters can be applied allowing views to be filtered to things like particular customerIds.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEmbedAccessTokenRequest(
    description="laborum",
    duration=170909,
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key="corporis",
                operator="explicabo",
                value="nobis",
            ),
        ],
        limit=315428,
        offset=607831,
        operator="nemo",
    ),
)

res = s.embeds.get_embed_access_token(req)

if res.embed_access_token_response is not None:
    # handle response
```