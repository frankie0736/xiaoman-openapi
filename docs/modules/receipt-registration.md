# 回款登记

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/receipt-registration.openapi.yaml`
- endpoints: `5`

## POST /v1/invoices/receiptRegistration/allocate

- operationId: `post_v1_invoices_receiptregistration_allocate`
- summary: 回款登记核销
- source: `../../sources/pages/api-3478295.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                       | type    | required | description                                   |
| -------------------------- | ------- | -------- | --------------------------------------------- |
| cash_collection_invoice_id | integer | no       | ID或编号选传一个。                                    |
| record_list                | array   | yes      | 核销明细，只能新增核销，不支持编辑已有核销。如需编辑，请删除明细内的对应回款单后再进行核销 |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/receiptRegistration/fields

- operationId: `get_v1_invoices_receiptregistration_fields`
- summary: 回款登记字段
- source: `../../sources/pages/api-3478292.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/receiptRegistration/info

- operationId: `get_v1_invoices_receiptregistration_info`
- summary: 回款登记详情
- source: `../../sources/pages/api-3484727.md`

### parameters

| in     | name                       | type    | required | description                              |
| ------ | -------------------------- | ------- | -------- | ---------------------------------------- |
| query  | cash_collection_invoice_id | integer | no       | 回款登记ID                                   |
| query  | cash_collection_invoice_no | string  | no       | 回款登记编号                                   |
| header | Authorization              | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/invoices/receiptRegistration/list

- operationId: `get_v1_invoices_receiptregistration_list`
- summary: 回款登记列表
- source: `../../sources/pages/api-3478294.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | start_time    | string  | no       | 创建/更新开始时间                                |
| query  | end_time      | string  | no       | 创建/更新截止时间                                |
| query  | count         | integer | no       | 每页数量                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | removed       | integer | no       | 设置=1时查询已删除的数据列表                          |
| query  | time_type     | integer | no       | 默认值1， 1更新时间，2创建时间                        |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/receiptRegistration/push

- operationId: `post_v1_invoices_receiptregistration_push`
- summary: 回款登记新建/编辑
- source: `../../sources/pages/api-3478293.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                       | type        | required | description                                                                              |
| -------------------------- | ----------- | -------- | ---------------------------------------------------------------------------------------- |
| cash_collection_invoice_id | integer     | no       | 回款登记ID，编辑时可传入                                                                            |
| cash_collection_invoice_no | string      | no       | 回款登记编号，编辑时可以传入                                                                           |
| collection_date            | string/date | no       | 回款日期                                                                                     |
| type                       | string      | no       | 回款方式，值为 /v1/invoices/receipt/types 接口返回列表中的值                                             |
| trade_no                   | string      | no       | 交易号/票据号                                                                                  |
| account_name               | string      | no       | 来款方                                                                                      |
| bank_name                  | string      | no       | 来款银行                                                                                     |
| bank_account               | string      | no       | 来款账户                                                                                     |
| remark                     | string      | no       | 备注                                                                                       |
| currency                   | string      | yes      | 币种                                                                                       |
| exchange_rate              | number      | no       | 汇率，100单位单据币种（兑CNY）                                                                       |
| exchange_rate_usd          | number      | no       | 汇率，100单位单据币种汇率（兑USD）                                                                     |
| amount                     | number      | yes      | 回款金额/客户打款金额（单据币种）                                                                        |
| real_amount                | number      | no       | 实到账金额（单据币种）                                                                              |
| company_id                 | integer     | no       | 关联客户ID                                                                                   |
| capital_account_id         | integer     | no       | 资金账户ID，值参考/v1/capitalAccount/list接口的资金账户ID                                               |
| handler                    | array       | no       | 认领业务员，新建时传入业务认领人和关联客户后，回款登记的状态为待核销，否则是待核销或者草稿，调试时请注意传入后的状态是否符合业务需求，注意有启用的回款登记的审批规则不符合上述。 |
| create_user                | integer     | no       | 创建人                                                                                      |
| record_list                | array       | no       | 暂时还不支持新建核销明细，还在开发中                                                                       |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
