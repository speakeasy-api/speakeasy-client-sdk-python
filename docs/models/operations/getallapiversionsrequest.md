# GetAllAPIVersionsRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `api_id`                                                 | *str*                                                    | :heavy_check_mark:                                       | The ID of the Api to retrieve.                           |
| `op`                                                     | [Optional[operations.Op]](../../models/operations/op.md) | :heavy_minus_sign:                                       | Configuration for filter operations                      |
| `metadata`                                               | Dict[str, List[*str*]]                                   | :heavy_minus_sign:                                       | Metadata to filter Apis on                               |