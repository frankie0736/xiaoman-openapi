# 付款单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/payment.openapi.yaml`
- endpoints: `3`

## GET /v1/paymentInvoice/fields

- operationId: `get_v1_paymentinvoice_fields`
- summary: 付款单字段
- source: `../../sources/pages/api-3483963.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/paymentInvoice/info

- operationId: `get_v1_paymentinvoice_info`
- summary: 付款单详情
- source: `../../sources/pages/api-3483962.md`

### parameters

| in     | name               | type    | required | description                              |
| ------ | ------------------ | ------- | -------- | ---------------------------------------- |
| query  | payment_invoice_id | integer | no       | 付款单ID ID或编号必须传其中一项                       |
| query  | payment_invoice_no | string  | no       | 付款单编号                                    |
| header | Authorization      | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/paymentInvoice/list

- operationId: `get_v1_paymentinvoice_list`
- summary: 付款单列表
- source: `../../sources/pages/api-3484721.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | time_type     | integer | no       | 时间筛选 1-按更新时间，2-按创建时间                     |
| query  | start_time    | string  | no       | 开始时间                                     |
| query  | end_time      | string  | no       | 截止时间                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | count         | integer | no       | 每页数量                                     |
| query  | removed       | integer | no       | 默认值: 0，设置=1时查询已删除的数据列表                   |
| query  | status        | integer | no       | 用单状态:1-草稿、2-待付款、3-已付款、4-已作废              |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
