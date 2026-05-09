# 回款单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/receipt.openapi.yaml`
- endpoints: `5`

## GET /v1/invoices/receipt/fields

- operationId: `get_v1_invoices_receipt_fields`
- summary: 回款单字段
- source: `../../sources/pages/api-3478276.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/receipt/info

- operationId: `get_v1_invoices_receipt_info`
- summary: 回款单详情
- source: `../../sources/pages/api-3478277.md`

### parameters

| in     | name               | type    | required | description                              |
| ------ | ------------------ | ------- | -------- | ---------------------------------------- |
| query  | cash_collection_id | integer | no       | 回款单ID                                    |
| query  | cash_collection_no | string  | no       | 回款单编号，与回款单ID二选一                          |
| header | Authorization      | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/receipt/list

- operationId: `get_v1_invoices_receipt_list`
- summary: 回款单列表
- source: `../../sources/pages/api-3478279.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | start_index   | string  | no       | 页码，默认1                                   |
| query  | count         | integer | no       | 每页条数，默认20                                |
| query  | start_time    | string  | no       | 更新时间开始日期                                 |
| query  | end_time      | string  | no       | 更新时间结束日期                                 |
| query  | removed       | string  | no       | 是否返回删除的回款单                               |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `multipart/form-data` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/receipt/push

- operationId: `post_v1_invoices_receipt_push`
- summary: 回款单新建/编辑
- source: `../../sources/pages/api-3478278.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                | type    | required | description                                                      |
| ------------------- | ------- | -------- | ---------------------------------------------------------------- |
| 12345678            | string  | no       | 自定义字段，若自定义单选字段，值来自/v1/invoices/order/fields中对应字段的ext_info中的一个或多个 |
| order_id            | integer | no       | 如果关联的是订单，则设置order_id,不要设置opportunity_id                          |
| collection_date     | string  | no       | 回款日期                                                             |
| amount              | integer | yes      | 回款金额(打款金额)                                                       |
| currency            | string  | yes      | 币种                                                               |
| exchange_rate       | number  | no       | 当前币种换人民币汇率，不传取系统取系统设置的汇率，与exchange_rate_usd可以同时传，但必须有其中一个        |
| finance_verify_date | string  | no       | 财务确认时间，可选字段(该字段废弃，请勿使用)                                          |
| comment             | string  | no       | 备注，可选字段                                                          |
| payee               | string  | no       | 财务确认人，可选                                                         |
| collect_status      | integer | no       | 回款状态，值为 1 已生效，0 未生效，默认0                                          |
| trade_no            | string  | no       | 交易号/票据号                                                          |
| cash_collection_no  | string  | no       | 回款单号                                                             |
| exchange_rate_usd   | number  | no       | 当前币种换美元汇率，不传系统取系统配置的汇率，与exchange_rate可以同时传，但必须有其中一个              |
| finance_verify_name | string  | no       | 财务确认人，可选字段(该字段废弃，请勿使用)                                           |
| capital_account_id  | integer | no       | 资金账户，值传入资金账户ID，/v1/capitalAccount/list. capital_account_id       |
| bank_charge         | number  | no       | 回款手续费                                                            |
| file_list           | array   | no       |                                                                  |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/receipt/types

- operationId: `get_v1_invoices_receipt_types`
- summary: 回款方式枚举
- source: `../../sources/pages/api-3485302.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
