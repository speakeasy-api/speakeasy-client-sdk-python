# Schema

A Schema represents an API schema for a particular Api and Version.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_id`                                                             | *str*                                                                | :heavy_check_mark:                                                   | The ID of the Api this Schema belongs to.                            |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp.                                                  |
| `description`                                                        | *str*                                                                | :heavy_check_mark:                                                   | A detailed description of the Schema.                                |
| `revision_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | An ID referencing this particular revision of the Schema.            |
| `version_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The version ID of the Api this Schema belongs to.                    |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The workspace ID this Schema belongs to.                             |