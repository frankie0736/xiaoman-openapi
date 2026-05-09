# devops相关

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/devops.openapi.yaml`
- endpoints: `6`

## POST /api/dingtalkwrite/deletedingtalkmember

- operationId: `post_api_dingtalkwrite_deletedingtalkmember`
- summary: 钉钉管理-删除账号
- source: `../../sources/pages/api-3496688.md`

### parameters

| in     | name             | type    | required | description                              |
| ------ | ---------------- | ------- | -------- | ---------------------------------------- |
| query  | dingtalk_user_id | integer | no       |                                          |
| query  | crm_user_id      | integer | no       |                                          |
| header | Authorization    | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /api/internal/prometheus/cisaveappversion

- operationId: `post_api_internal_prometheus_cisaveappversion`
- summary: app版本发布
- source: `../../sources/pages/api-3496687.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `multipart/form-data` schema: `object`

| name                | type    | required | description |
| ------------------- | ------- | -------- | ----------- |
| app_key             | string  | yes      |             |
| version             | string  | yes      |             |
| app_name            | string  | no       |             |
| app_platform        | string  | no       |             |
| version_description | string  | no       |             |
| secret_key          | string  | no       |             |
| min_version         | integer | no       |             |
| file_name           | string  | no       |             |
| file_size           | string  | no       |             |
| file_url            | string  | no       |             |
| file_md5            | string  | no       |             |
| content             | string  | no       |             |
| extension_data      | string  | no       |             |
| is_diff             | integer | no       |             |
| is_ABTest           | integer | no       |             |
| status              | integer | no       |             |
| project_id          | integer | no       |             |
| branch              | string  | no       |             |
| pipeline_tag        | string  | no       |             |
| pipeline_id         | integer | no       |             |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /api/internal/sobot/getsobottoken

- operationId: `get_api_internal_sobot_getsobottoken`
- summary: 获取智齿token
- source: `../../sources/pages/api-3496685.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /api/internal/sobot/refreshsobottoken

- operationId: `get_api_internal_sobot_refreshsobottoken`
- summary: 智齿刷新接口
- source: `../../sources/pages/api-3496686.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/dingtalk/webhook

- operationId: `post_v1_dingtalk_webhook`
- summary: 钉钉回调
- source: `../../sources/pages/api-3496683.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/tapd/webhook

- operationId: `get_v1_tapd_webhook`
- summary: tapd回调接口
- source: `../../sources/pages/api-3496684.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
