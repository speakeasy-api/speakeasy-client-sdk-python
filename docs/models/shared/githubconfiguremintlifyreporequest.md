# GithubConfigureMintlifyRepoRequest

A request to configure a GitHub repository for mintlify


## Fields

| Field                        | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `input`                      | *str*                        | :heavy_check_mark:           | The input OpenAPI document   |
| `org`                        | *str*                        | :heavy_check_mark:           | The GitHub organization name |
| `overlays`                   | List[*str*]                  | :heavy_check_mark:           | The overlays to apply        |
| `repo`                       | *str*                        | :heavy_check_mark:           | The GitHub repository name   |