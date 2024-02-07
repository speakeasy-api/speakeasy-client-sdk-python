# APIInput

An Api is representation of a API (a collection of API Endpoints) within the Speakeasy Platform.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `api_id`                                                                                 | *str*                                                                                    | :heavy_check_mark:                                                                       | The ID of this Api. This is a human-readable name (subject to change).                   |
| `description`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | A detailed description of the Api.                                                       |
| `version_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | The version ID of this Api. This is semantic version identifier.                         |
| `meta_data`                                                                              | Dict[str, List[*str*]]                                                                   | :heavy_minus_sign:                                                                       | A set of values associated with a meta_data key. This field is only set on get requests. |