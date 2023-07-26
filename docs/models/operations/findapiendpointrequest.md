# FindAPIEndpointRequest


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `api_id`                                                                             | *str*                                                                                | :heavy_check_mark:                                                                   | The ID of the Api the ApiEndpoint belongs to.                                        |
| `display_name`                                                                       | *str*                                                                                | :heavy_check_mark:                                                                   | The displayName of the ApiEndpoint to find (set by operationId from OpenAPI schema). |
| `version_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | The version ID of the Api the ApiEndpoint belongs to.                                |