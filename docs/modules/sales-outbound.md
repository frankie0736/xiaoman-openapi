# 销售出库单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/sales-outbound.openapi.yaml`
- endpoints: `5`

## GET /v1/invoices/outbound/fields

- operationId: `get_v1_invoices_outbound_fields`
- summary: 销售出库单字段
- source: `../../sources/pages/api-3484728.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/invoices/outbound/info

- operationId: `get_v1_invoices_outbound_info`
- summary: 销售出库单详情
- source: `../../sources/pages/api-3483515.md`

### parameters

| in     | name                | type    | required | description                                      |
| ------ | ------------------- | ------- | -------- | ------------------------------------------------ |
| query  | outbound_invoice_id | integer | no       | 销售出库单ID，值可以来自/v1/invoices/outbound/list          |
| query  | serial_id           | string  | no       | 销售出库单号，与ID必须选择一项 值可以来自/v1/invoices/outbound/list |
| header | Authorization       | string  | yes      | 从/v1/oauth2/access_token获取到的access_token         |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/invoices/outbound/list

- operationId: `get_v1_invoices_outbound_list`
- summary: 销售出库单列表
- source: `../../sources/pages/api-3484729.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | start_time    | string  | no       | 创建/更新开始时间                                |
| query  | end_time      | string  | no       | 创建/更新截止时间                                |
| query  | time_type     | integer | no       | 默认值1， 1更新时间，2创建时间                        |
| query  | count         | integer | no       | 每页数量                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | removed       | integer | no       | 默认值: 0，设置=1时查询已删除的数据列表                   |
| query  | status        | integer | no       | 销售出库单状态：1-待出库，2-已出库                      |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/invoices/outbound/push

- operationId: `post_v1_invoices_outbound_push`
- summary: 新增/编辑销售出库单
- source: `../../sources/pages/api-3478296.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                 | type    | required | description                         |
| -------------------- | ------- | -------- | ----------------------------------- |
| status               | integer | no       |                                     |
| discount_rate        | integer | no       |                                     |
| currency             | string  | no       |                                     |
| exchange_rate        | number  | no       |                                     |
| exchange_rate_usd    | number  | no       |                                     |
| source_type          | integer | no       |                                     |
| invoice_warehouse_id | integer | no       | 值来自于/v1/warehouse/list              |
| company_id           | integer | no       | 值来自于/v1/company/list                |
| handler              | array   | yes      | 值来自于/v1/user/list                   |
| record_list          | array   | yes      |                                     |
| outbound_invoice_id  | integer | no       | 编辑时必传 值来自/v1/invoices/outbound/list |
| serial_id            | string  | no       | 销售出库单号                              |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/outbound/remove

- operationId: `post_v1_invoices_outbound_remove`
- summary: 销售出库单删除
- source: `../../sources/pages/api-3484730.md`

### parameters

| in     | name                | type    | required | description                                            |
| ------ | ------------------- | ------- | -------- | ------------------------------------------------------ |
| query  | outbound_invoice_id | integer | no       | 销售出库单ID 值来自/v1/invoices/outbound/list                  |
| query  | serial_id           | string  | no       | 销售出库单号 与销售出库单ID 必须传递其中一个 值来自/v1/invoices/outbound/list |
| header | Authorization       | string  | yes      | 从/v1/oauth2/access_token获取到的access_token               |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
