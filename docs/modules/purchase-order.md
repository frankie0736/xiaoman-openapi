# 采购订单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/purchase-order.openapi.yaml`
- endpoints: `5`

## GET /v1/purchaseOrder/fields

- operationId: `get_v1_purchaseorder_fields`
- summary: 采购订单字段
- source: `../../sources/pages/api-3484725.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/purchaseOrder/fields/selector

- operationId: `get_v1_purchaseorder_fields_selector`
- summary: 采购订单状态
- source: `../../sources/pages/api-3484726.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| query  | field         | string | no       |                                          |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/purchaseOrder/info

- operationId: `get_v1_purchaseorder_info`
- summary: 采购订单详情
- source: `../../sources/pages/api-3478250.md`

### parameters

| in     | name              | type    | required | description                              |
| ------ | ----------------- | ------- | -------- | ---------------------------------------- |
| query  | purchase_order_id | integer | no       | 采购订单ID                                   |
| query  | purchase_order_no | string  | no       | 采购订单编码，可与采购订单ID二选一                       |
| header | Authorization     | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/purchaseOrder/list

- operationId: `get_v1_purchaseorder_list`
- summary: 采购订单列表
- source: `../../sources/pages/api-3478331.md`

### parameters

| in     | name          | type    | required | description                                       |
| ------ | ------------- | ------- | -------- | ------------------------------------------------- |
| query  | start_time    | string  | no       | 创建/更新开始时间                                         |
| query  | end_time      | string  | no       | 创建/更新截止时间                                         |
| query  | count         | integer | no       | 每页数量，默认20                                         |
| query  | start_index   | integer | no       | 页码，默认1                                            |
| query  | removed       | integer | no       | 默认值: 0，设置=1时查询已删除的数据列表                            |
| query  | time_type     | integer | no       | 默认值1， 1更新时间，2创建时间                                 |
| query  | status        | integer | no       | 采购订单状态，值为/v1/purchaseOrder/fields/selector接口的状态ID |
| query  | status_name   | string  | no       | 采购订单状态名称                                          |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token          |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/purchaseOrder/push

- operationId: `post_v1_purchaseorder_push`
- summary: 采购订单新增/编辑
- source: `../../sources/pages/api-3478249.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                 | type         | required | description                                                             |
| -------------------- | ------------ | -------- | ----------------------------------------------------------------------- |
| 3137211747           | string       | no       | 采购订单自定义字段。字段名称为/v1/purchaseOrder/fields 获取到的自定义字段ID                     |
| purchase_order_id    | integer      | no       | 采购订单ID，编辑时必填                                                            |
| purchase_order_no    | string       | no       | 采购订单编号                                                                  |
| supplier_id          | integer      | no       | 供应商ID，新建时必填，来自供应商模块的.supplier_id                                        |
| supplier_contact     | integer      | no       | 供应商联系人ID，选填，来自供应商模块contact_list.supplier_contact_id                     |
| currency             | string       | no       | 币种，新建是必填，传入值可以参考订单的/v1/invoices/order/orderEnums字段里面的currency_list.code |
| exchange_rate        | number/float | no       | 汇率(兑CNY人民币)                                                             |
| exchange_rate_usd    | number/float | no       | 汇率(兑USD美元)                                                              |
| purchase_date        | string/date  | no       | 采购日期，非必填，缺省值为当前日期，例如2024-04-29                                          |
| delivery_date        | string/date  | no       | 交货日期，非必填                                                                |
| remark               | string       | no       | 备注，非必填，例如2024-04-29                                                     |
| refer_order_id       | integer      | no       | 关联的销售订单ID，来自销售订单模块的order_id                                             |
| creator              | integer      | no       | 采购订单创建人，默认为请求接口的当前用户，传入值来自/v1/user/list中的user_id                        |
| handler              | array        | no       | 采购订单处理人                                                                 |
| status               | integer      | no       | 采购订单状态ID，值为/v1/purchaseOrder/fields/selector接口的状态ID                     |
| amount               | number       | no       | 采购订单金额，新建时必填                                                            |
| product_total_amount | number       | no       | 采购订单产品总金额                                                               |
| cost_list            | array        | no       | 费用列表                                                                    |
| product_list         | array        | no       | 采购订单产品明细列表                                                              |
| attachments          | array        | no       | 附件，可访问的文件url                                                            |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
