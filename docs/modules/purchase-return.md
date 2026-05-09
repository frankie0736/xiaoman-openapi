# 采购退货单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/purchase-return.openapi.yaml`
- endpoints: `5`

## GET /v1/invoices/purchaseReturn/fields

- operationId: `get_v1_invoices_purchasereturn_fields`
- summary: 采购退货单字段
- source: `../../sources/pages/api-3484291.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/purchaseReturn/info

- operationId: `get_v1_invoices_purchasereturn_info`
- summary: 采购退货单-详情
- source: `../../sources/pages/api-3484265.md`

### parameters

| in     | name                        | type   | required | description                                 |
| ------ | --------------------------- | ------ | -------- | ------------------------------------------- |
| query  | warehouse_return_invoice_id | string | no       | 采购退货单id 值来自/v1/invoices/purchaseReturn/list |
| query  | serial_id                   | string | no       | 采购退货单编号 值来自/v1/invoices/purchaseReturn/list |
| header | Authorization               | string | yes      | 从/v1/oauth2/access_token获取到的access_token    |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/purchaseReturn/list

- operationId: `get_v1_invoices_purchasereturn_list`
- summary: 采购退货单-列表
- source: `../../sources/pages/api-3484264.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| query  | start_time    | string | no       | 开始时间                                     |
| query  | end_time      | string | no       | 结束时间                                     |
| query  | start_index   | number | no       | 页码                                       |
| query  | count         | number | no       | 每页条数                                     |
| query  | removed       | number | no       | 默认0，1表示查询已删除的数据列表                        |
| query  | status        | string | no       | 对应的状态值1是                                 |
| query  | time_type     | string | no       | 时间查询参数，默认为1，1是更新时间排序，2是创建时间排序            |
| query  | serial_id     | string | no       | 采购退货单号                                   |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/purchaseReturn/push

- operationId: `post_v1_invoices_purchasereturn_push`
- summary: 采购退货单-新建/编辑
- source: `../../sources/pages/api-3484292.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                        | type    | required | description                         |
| --------------------------- | ------- | -------- | ----------------------------------- |
| serial_id                   | string  | no       | 采购退货单编号                             |
| currency                    | string  | yes      |                                     |
| exchange_rate               | number  | no       |                                     |
| exchange_rate_usd           | number  | no       |                                     |
| warehouse_invoice_time      | string  | yes      |                                     |
| supplier_id                 | integer | yes      | 值来自/v1/supplier/list                |
| remark                      | string  | yes      |                                     |
| record_list                 | array   | no       |                                     |
| product_total_count         | integer | yes      |                                     |
| attachment                  | array   | yes      |                                     |
| discount_rate               | integer | yes      |                                     |
| handler                     | array   | yes      | 值来自/v1/user/list                    |
| invoice_warehouse_id        | integer | yes      | 值来自/v1/warehouse/list               |
| warehouse_return_invoice_id | integer | no       | 值来自/v1/invoices/purchaseReturn/list |
| user_id                     | integer | no       | 值来自/v1/user/list                    |
| status                      | integer | yes      | 状态为1是草稿，2为已完成                       |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/purchaseReturn/remove

- operationId: `post_v1_invoices_purchasereturn_remove`
- summary: 采购退货单-删除
- source: `../../sources/pages/api-3484293.md`

### parameters

| in     | name                        | type    | required | description                                 |
| ------ | --------------------------- | ------- | -------- | ------------------------------------------- |
| query  | warehouse_return_invoice_id | integer | yes      | 采购退货id 值来自/v1/invoices/purchaseInbound/list |
| header | Authorization               | string  | yes      | 从/v1/oauth2/access_token获取到的access_token    |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
