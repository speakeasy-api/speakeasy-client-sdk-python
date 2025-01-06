# CodeSampleSchemaInput


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `languages`                                            | List[*str*]                                            | :heavy_check_mark:                                     | A list of languages to generate code samples for       |
| `schema_file`                                          | [shared.SchemaFile](../../models/shared/schemafile.md) | :heavy_check_mark:                                     | The OpenAPI file to be uploaded                        |
| `package_name`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | The name of the package                                |
| `sdk_class_name`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | The SDK class name                                     |