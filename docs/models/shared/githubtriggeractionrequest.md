# GithubTriggerActionRequest

A request to trigger an action on a GitHub target


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `gen_lock_id`                  | *str*                          | :heavy_check_mark:             | The generation lock ID         |
| `org`                          | *str*                          | :heavy_check_mark:             | The GitHub organization name   |
| `repo_name`                    | *str*                          | :heavy_check_mark:             | The GitHub repository name     |
| `target_name`                  | *Optional[str]*                | :heavy_minus_sign:             | The target name for the action |