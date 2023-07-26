# GetAllAPIVersionsRequest


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `api_id`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | The ID of the Api to retrieve.                                                  |
| `metadata`                                                                      | dict[str, list[*str*]]                                                          | :heavy_minus_sign:                                                              | Metadata to filter Apis on                                                      |
| `op`                                                                            | [Optional[GetAllAPIVersionsOp]](../../models/operations/getallapiversionsop.md) | :heavy_minus_sign:                                                              | Configuration for filter operations                                             |