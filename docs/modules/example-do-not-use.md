# 示例接口（勿用）

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/example-do-not-use.openapi.yaml`
- endpoints: `2`

## POST /api

- operationId: `post_api`
- summary: 例子列表
- source: `../../sources/pages/api-3486416.md`

### parameters

| in     | name          | type    | required | description       |
| ------ | ------------- | ------- | -------- | ----------------- |
| query  | version       | integer | yes      | 版本                |
| query  | method        | string  | yes      | 请求的接口             |
| query  | sign          | string  | yes      | 参数签名              |
| query  | timestamp     | integer | yes      | 请求时间戳             |
| query  | client_id     | string  | yes      | 应该ID              |
| header | Authorization | string  | yes      | 带入有效的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name      | type    | required | description                                          |
| --------- | ------- | -------- | ---------------------------------------------------- |
| page      | integer | no       | 页码，默认1                                               |
| page_size | integer | no       | 每页数量，默认10                                            |
| status    | array   | no       | 查询的状态，枚举中可以从/example/fields接口传入type=status，使用返回值中的id |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /api1

- operationId: `post_api1`
- summary: 例子枚举值查询
- source: `../../sources/pages/api-3486417.md`

### parameters

| in     | name          | type    | required | description       |
| ------ | ------------- | ------- | -------- | ----------------- |
| query  | version       | integer | yes      | 版本                |
| query  | method        | string  | yes      | 请求的接口             |
| query  | sign          | string  | yes      | 参数签名              |
| query  | timestamp     | integer | yes      | 请求时间戳             |
| query  | client_id     | string  | yes      | 应该ID              |
| header | Authorization | string  | yes      | 带入有效的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name | type   | required | description |
| ---- | ------ | -------- | ----------- |
| type | string | no       |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
