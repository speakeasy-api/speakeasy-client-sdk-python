# Requests
(*requests*)

## Overview

REST APIs for retrieving request information

### Available Operations

* [generate_request_postman_collection](#generate_request_postman_collection) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](#get_request_from_event_log) - Get information about a particular request.
* [query_event_log](#query_event_log) - Query the event log to retrieve a list of requests.

## generate_request_postman_collection

Generates a Postman collection for a particular request. 
Allowing it to be replayed with the same inputs that were captured by the SDK.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GenerateRequestPostmanCollectionRequest(
    request_id='Architect',
)

res = s.requests.generate_request_postman_collection(req)

if res.postman_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GenerateRequestPostmanCollectionRequest](../../models/operations/generaterequestpostmancollectionrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GenerateRequestPostmanCollectionResponse](../../models/operations/generaterequestpostmancollectionresponse.md)**


## get_request_from_event_log

Get information about a particular request.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetRequestFromEventLogRequest(
    request_id='Chevrolet',
)

res = s.requests.get_request_from_event_log(req)

if res.unbounded_request is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetRequestFromEventLogRequest](../../models/operations/getrequestfromeventlogrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetRequestFromEventLogResponse](../../models/operations/getrequestfromeventlogresponse.md)**


## query_event_log

Supports retrieving a list of request captured by the SDK for this workspace.
Allows the filtering of requests on a number of criteria such as ApiID, VersionID, Path, Method, etc.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.QueryEventLogRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key='<key>',
                operator='Cotton',
                value='Interactions',
            ),
        ],
        limit=6323,
        offset=788512,
        operator='Practical',
    ),
)

res = s.requests.query_event_log(req)

if res.bounded_requests is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.QueryEventLogRequest](../../models/operations/queryeventlogrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.QueryEventLogResponse](../../models/operations/queryeventlogresponse.md)**

