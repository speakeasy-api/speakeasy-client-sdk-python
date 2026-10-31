# GithubPublishingPRResponse

Open generation PRs pending publishing


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `pending_version`                                                                  | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `pull_request`                                                                     | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `pull_request_metadata`                                                            | [Optional[shared.PullRequestMetadata]](../../models/shared/pullrequestmetadata.md) | :heavy_minus_sign:                                                                 | This can only be populated when the github app is installed for a repo             |