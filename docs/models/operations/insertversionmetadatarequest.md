# InsertVersionMetadataRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `version_metadata_input`                                                   | [shared.VersionMetadataInput](../../models/shared/versionmetadatainput.md) | :heavy_check_mark:                                                         | A JSON representation of the metadata to insert.                           |
| `api_id`                                                                   | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the Api to insert metadata for.                                  |
| `version_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | The version ID of the Api to insert metadata for.                          |