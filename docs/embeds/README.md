# embeds

## Overview

REST APIs for managing embeds

### Available Operations

* [get_embed_access_token](#get_embed_access_token) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](#get_valid_embed_access_tokens) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](#revoke_embed_access_token) - Revoke an embed access EmbedToken.

## get_embed_access_token

Returns an embed access token for the current workspace. This can be used to authenticate access to externally embedded content.
Filters can be applied allowing views to be filtered to things like particular customerIds.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEmbedAccessTokenRequest(
    description='laborum',
    duration=170909,
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key='corporis',
                operator='explicabo',
                value='nobis',
            ),
        ],
        limit=315428,
        offset=607831,
        operator='nemo',
    ),
)

res = s.embeds.get_embed_access_token(req)

if res.embed_access_token_response is not None:
    # handle response
```

## get_valid_embed_access_tokens

Get all valid embed access tokens for the current workspace.

### Example Usage

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

## revoke_embed_access_token

Revoke an embed access EmbedToken.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RevokeEmbedAccessTokenRequest(
    token_id='minima',
)

res = s.embeds.revoke_embed_access_token(req)

if res.status_code == 200:
    # handle response
```
