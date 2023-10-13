# RegisterSchemaRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request_body`                                                                    | [RegisterSchemaRequestBody](../../models/operations/registerschemarequestbody.md) | :heavy_check_mark:                                                                | The schema file to upload provided as a multipart/form-data file segment.         |
| `api_id`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the Api to get the schema for.                                          |
| `version_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | The version ID of the Api to delete metadata for.                                 |