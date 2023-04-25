# query_event_log
Available in: `requests`

Supports retrieving a list of request captured by the SDK for this workspace.
Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.QueryEventLogRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key="ipsam",
                operator="id",
                value="possimus",
            ),
            shared.Filter(
                key="aut",
                operator="quasi",
                value="error",
            ),
            shared.Filter(
                key="temporibus",
                operator="laborum",
                value="quasi",
            ),
            shared.Filter(
                key="reiciendis",
                operator="voluptatibus",
                value="vero",
            ),
        ],
        limit=468651,
        offset=509624,
        operator="voluptatibus",
    ),
)

res = s.requests.query_event_log(req)

if res.bounded_requests is not None:
    # handle response
```