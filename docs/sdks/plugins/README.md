# Plugins
(*plugins*)

## Overview

REST APIs for managing and running plugins

### Available Operations

* [get_plugins](#get_plugins) - Get all plugins for the current workspace.
* [run_plugin](#run_plugin) - Run a plugin
* [upsert_plugin](#upsert_plugin) - Upsert a plugin

## get_plugins

Get all plugins for the current workspace.

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.plugins.get_plugins()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetPluginsResponse](../../models/operations/getpluginsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## run_plugin

Run a plugin

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RunPluginRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key='<key>',
                operator='string',
                value='string',
            ),
        ],
        limit=669298,
        offset=94585,
        operator='string',
    ),
    plugin_id='string',
)

res = s.plugins.run_plugin(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.RunPluginRequest](../../models/operations/runpluginrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.RunPluginResponse](../../models/operations/runpluginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## upsert_plugin

Upsert a plugin

### Example Usage

```python
import dateutil.parser
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.Plugin(
    code='string',
    plugin_id='string',
    title='string',
    workspace_id='string',
)

res = s.plugins.upsert_plugin(req)

if res.plugin is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `request`                                      | [shared.Plugin](../../models/shared/plugin.md) | :heavy_check_mark:                             | The request object to use for the request.     |


### Response

**[operations.UpsertPluginResponse](../../models/operations/upsertpluginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
