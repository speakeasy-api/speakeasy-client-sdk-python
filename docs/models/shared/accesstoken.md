# AccessToken

An AccessToken is a token that can be used to authenticate with the Speakeasy API.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `access_token`                                                   | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `claims`                                                         | [shared.Claims](../../models/shared/claims.md)                   | :heavy_check_mark:                                               | N/A                                                              |
| `user`                                                           | [shared.AccessTokenUser](../../models/shared/accesstokenuser.md) | :heavy_check_mark:                                               | N/A                                                              |
| `feature_flags`                                                  | List[[shared.FeatureFlag](../../models/shared/featureflag.md)]   | :heavy_minus_sign:                                               | N/A                                                              |
| `workspaces`                                                     | List[[shared.Workspaces](../../models/shared/workspaces.md)]     | :heavy_minus_sign:                                               | N/A                                                              |