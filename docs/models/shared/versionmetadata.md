# VersionMetadata

A set of keys and associated values, attached to a particular version of an Api.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_id`                                                             | *str*                                                                | :heavy_check_mark:                                                   | The ID of the Api this Metadata belongs to.                          |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp.                                                  |
| `meta_key`                                                           | *str*                                                                | :heavy_check_mark:                                                   | The key for this metadata.                                           |
| `meta_value`                                                         | *str*                                                                | :heavy_check_mark:                                                   | One of the values for this metadata.                                 |
| `version_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The version ID of the Api this Metadata belongs to.                  |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The workspace ID this Metadata belongs to.                           |