# SchemaDiff

A SchemaDiff represents a diff of two Schemas.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `additions`                                                                      | list[*str*]                                                                      | :heavy_check_mark:                                                               | Holds every addition change in the diff.                                         |
| `deletions`                                                                      | list[*str*]                                                                      | :heavy_check_mark:                                                               | Holds every deletion change in the diff.                                         |
| `modifications`                                                                  | dict[str, [SchemaDiffValueChange](../../models/shared/schemadiffvaluechange.md)] | :heavy_check_mark:                                                               | Holds every modification change in the diff.                                     |