# CreateSchemaStoreItemRequestBody


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `format_`                                                      | [operations.Format](../../models/operations/format_.md)        | :heavy_check_mark:                                             | The format of the OpenAPI specification.                       |
| `package_name`                                                 | *str*                                                          | :heavy_check_mark:                                             | The package name to use in code snippets / quickstart.         |
| `sdk_classname`                                                | *str*                                                          | :heavy_check_mark:                                             | The classname of the SDK to use in code snippets / quickstart. |
| `spec`                                                         | *str*                                                          | :heavy_check_mark:                                             | The OpenAPI specification to store.                            |