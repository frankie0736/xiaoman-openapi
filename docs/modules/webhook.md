# 消息推送

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/webhook.openapi.yaml`
- endpoints: `11`

## GET /v1/subscribe

- operationId: `get_v1_subscribe`
- summary: 获取订阅配置列表
- source: `../../sources/pages/api-3497061.md`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/subscribe

- operationId: `post_v1_subscribe`
- summary: 创建订阅配置
- source: `../../sources/pages/api-3497012.md`

### requestBody
- contentType: `application/json` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## DELETE /v1/subscribe/{subscribe_type}

- operationId: `delete_v1_subscribe_by_subscribe_type`
- summary: 删除订阅配置
- source: `../../sources/pages/api-3497055.md`

### parameters

| in   | name           | type   | required | description |
| ---- | -------------- | ------ | -------- | ----------- |
| path | subscribe_type | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/subscribe/{subscribe_type}

- operationId: `get_v1_subscribe_by_subscribe_type`
- summary: 获取订阅配置详情
- source: `../../sources/pages/api-3497060.md`

### parameters

| in   | name           | type   | required | description |
| ---- | -------------- | ------ | -------- | ----------- |
| path | subscribe_type | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## PUT /v1/subscribe/{subscribe_type}

- operationId: `put_v1_subscribe_by_subscribe_type`
- summary: 修改订阅配置
- source: `../../sources/pages/api-3497054.md`

### parameters

| in   | name           | type   | required | description |
| ---- | -------------- | ------ | -------- | ----------- |
| path | subscribe_type | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name              | type   | required | description |
| ----------------- | ------ | -------- | ----------- |
| subscribe_type    | string | yes      |             |
| subscribe_configs | array  | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## DELETE /v1/webhook

- operationId: `delete_v1_webhook`
- summary: 删除回调配置
- source: `../../sources/pages/api-3497058.md`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/webhook

- operationId: `get_v1_webhook`
- summary: 获取回调配置
- source: `../../sources/pages/api-3497057.md`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/webhook

- operationId: `post_v1_webhook`
- summary: 创建回调配置
- source: `../../sources/pages/api-3497011.md`

### requestBody
- contentType: `application/json` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## PUT /v1/webhook

- operationId: `put_v1_webhook`
- summary: 修改回调配置
- source: `../../sources/pages/api-3497056.md`

### requestBody
- contentType: `application/json` schema: `object`

| name         | type   | required | description |
| ------------ | ------ | -------- | ----------- |
| callback_url | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/webhook/regenerate-secret

- operationId: `post_v1_webhook_regenerate_secret`
- summary: 重新生成加密密钥
- source: `../../sources/pages/api-3497059.md`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/webhook/test

- operationId: `post_v1_webhook_test`
- summary: 测试回调接口
- source: `../../sources/pages/api-3497013.md`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
