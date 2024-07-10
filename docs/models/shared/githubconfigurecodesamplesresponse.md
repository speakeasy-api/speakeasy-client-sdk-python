# GithubConfigureCodeSamplesResponse

A response to configure GitHub code samples


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `code_sample_overlay_registry_url`                                 | *str*                                                              | :heavy_check_mark:                                                 | The URL of the code sample overlay registry                        |
| `source`                                                           | [shared.WorkflowDocument](../../models/shared/workflowdocument.md) | :heavy_check_mark:                                                 | A document referenced by a workflow                                |
| `gh_action_id`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The ID of the GitHub action that was dispatched                    |