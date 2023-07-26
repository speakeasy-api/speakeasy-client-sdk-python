# UpsertAPIEndpointRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `api_endpoint_input`                                               | [shared.APIEndpointInput](../../models/shared/apiendpointinput.md) | :heavy_check_mark:                                                 | A JSON representation of the ApiEndpoint to upsert.                |
| `api_endpoint_id`                                                  | *str*                                                              | :heavy_check_mark:                                                 | The ID of the ApiEndpoint to upsert.                               |
| `api_id`                                                           | *str*                                                              | :heavy_check_mark:                                                 | The ID of the Api the ApiEndpoint belongs to.                      |
| `version_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | The version ID of the Api the ApiEndpoint belongs to.              |