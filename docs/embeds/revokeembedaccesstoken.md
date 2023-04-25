# revoke_embed_access_token
Available in: `embeds`

Revoke an embed access EmbedToken.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RevokeEmbedAccessTokenRequest(
    token_id="minima",
)

res = s.embeds.revoke_embed_access_token(req)

if res.status_code == 200:
    # handle response
```