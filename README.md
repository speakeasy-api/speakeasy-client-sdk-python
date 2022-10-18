# speakeasy-client-sdk-python

This is the Speakeasy API Client SDK for Python. It is generated from our OpenAPI spec found at https://docs.speakeasyapi.dev/openapi.yaml and used for interacting with the [Speakeasy API](https://docs.speakeasyapi.dev/docs/speakeasy-api/speakeasy-api).

This SDK was generated using Speakeasy's SDK Generator. For more information on how to use the generator to generate your own SDKs, please see the [Speakeasy Client SDK Generator Docs](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks).

## Installation

```bash
pip install speakeasy-client-sdk-python
```

## Example usage
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY" # Replace with your API key from your Speakeasy Workspace
        )
    )
)

req = operations.GetApisRequest(
    query_params=operations.GetApisQueryParams(
        metadata={'label': ['1']},
        op=operations.GetApisOp(and_=True)
    )
)

res = s.get_apis(req)

if res.status_code == 200:
    print(res.apis)
else:
    print(res.error)

```