<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.artifacts.create_remote_source()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

async def main():
    async with Speakeasy(
        security=shared.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as speakeasy:

        res = await speakeasy.artifacts.create_remote_source_async()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->