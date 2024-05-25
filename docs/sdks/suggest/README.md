# Suggest
(*suggest*)

## Overview

REST APIs for managing LLM OAS suggestions

### Available Operations

* [suggest_operation_i_ds](#suggest_operation_i_ds) - Generate operation ID suggestions.

## suggest_operation_i_ds

Get suggestions from an LLM model for improving the operationIDs in the provided schema.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.suggest.suggest_operation_i_ds(request=operations.SuggestOperationIDsRequestBody(
    schema=operations.Schema(
        content='0xb2de88c98a'.encode(),
        file_name='your_file_here',
    ),
))

if res.suggestion is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.SuggestOperationIDsRequestBody](../../models/operations/suggestoperationidsrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.SuggestOperationIDsResponse](../../models/operations/suggestoperationidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
