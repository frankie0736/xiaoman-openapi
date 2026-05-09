# 采购入库单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/purchase-inbound.openapi.yaml`
- endpoints: `5`

## GET /v1/invoices/purchaseInbound/fields

- operationId: `get_v1_invoices_purchaseinbound_fields`
- summary: 采购入库单字段
- source: `../../sources/pages/api-3484299.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/purchaseInbound/info

- operationId: `get_v1_invoices_purchaseinbound_info`
- summary: 采购入库单-详情
- source: `../../sources/pages/api-3484298.md`

### parameters

| in     | name               | type    | required | description                              |
| ------ | ------------------ | ------- | -------- | ---------------------------------------- |
| query  | inbound_invoice_id | integer | no       | 采购入库单id                                  |
| query  | serial_id          | string  | no       | 采购入库单编号                                  |
| header | Authorization      | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/purchaseInbound/list

- operationId: `get_v1_invoices_purchaseinbound_list`
- summary: 采购入库单-列表
- source: `../../sources/pages/api-3484297.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | start_time    | string  | no       | 开始时间                                     |
| query  | end_time      | string  | no       | 结束时间                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | count         | number  | no       | 页面数量                                     |
| query  | removed       | number  | no       | 默认0，1表示查询已删除的数据列表                        |
| query  | status        | string  | no       | 对应的状态值1是                                 |
| query  | time_type     | integer | no       | 时间查询参数，默认为1，1是更新时间排序，2是创建时间排序            |
| query  | serial_id     | string  | no       | 采购入库单号                                   |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/invoices/purchaseInbound/push

- operationId: `post_v1_invoices_purchaseinbound_push`
- summary: 采购入库单-新建/编辑
- source: `../../sources/pages/api-3484333.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/x-msgpack` schema: `object`

| name                   | type    | required | description                                   |
| ---------------------- | ------- | -------- | --------------------------------------------- |
| supplier_id            | integer | yes      | 值来自于/v1/supplier/list                         |
| currency               | string  | yes      | 如果传入不能为空                                      |
| exchange_rate          | number  | no       | 如果传入不能为空                                      |
| exchange_rate_usd      | number  | no       | 如果传入不能为空                                      |
| serial_id              | string  | no       | 值来自于/v1/invoices/purchaseInbound/list         |
| warehouse_invoice_time | string  | no       | 如果传入不能为空                                      |
| remark                 | string  | no       |                                               |
| discount_rate          | integer | no       |                                               |
| discount               | number  | no       |                                               |
| handler                | array   | yes      | 传入处理人对应的user_id 值来自于/v1/user/list             |
| record_list            | array   | yes      |                                               |
| invoice_warehouse_id   | integer | yes      | 值来自于/v1/warehouse/list                        |
| inbound_id             | integer | no       | 编辑时需要传入 值来自于/v1/invoices/purchaseInbound/list |
| status                 | integer | yes      | 状态为1是草稿，2为已完成                                 |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/invoices/purchaseInbound/remove

- operationId: `post_v1_invoices_purchaseinbound_remove`
- summary: 采购入库单-删除
- source: `../../sources/pages/api-3484312.md`

### parameters

| in     | name               | type    | required | description                              |
| ------ | ------------------ | ------- | -------- | ---------------------------------------- |
| query  | inbound_invoice_id | integer | no       | 采购入库单ID                                  |
| query  | serial_id          | string  | no       | 采购入库单编号                                  |
| header | Authorization      | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
