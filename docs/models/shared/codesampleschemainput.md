# CodeSampleSchemaInput


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `language`                                             | *str*                                                  | :heavy_check_mark:                                     | The language to generate code samples for              |
| `schema_file`                                          | [shared.SchemaFile](../../models/shared/schemafile.md) | :heavy_check_mark:                                     | The OpenAPI file to be uploaded                        |
| `operation_ids`                                        | List[*str*]                                            | :heavy_minus_sign:                                     | A list of operations IDs to generate code samples for  |
| `package_name`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | The name of the package                                |
| `sdk_class_name`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | The SDK class name                                     |