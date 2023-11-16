# SchemaDiff

A SchemaDiff represents a diff of two Schemas.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `additions`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | Holds every addition change in the diff.                            |
| `deletions`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | Holds every deletion change in the diff.                            |
| `modifications`                                                     | Dict[str, [shared.ValueChange](../../models/shared/valuechange.md)] | :heavy_check_mark:                                                  | Holds every modification change in the diff.                        |