# 销售订单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/sales-order.openapi.yaml`
- endpoints: `6`

## GET /v1/invoices/order/fields

- operationId: `get_v1_invoices_order_fields`
- summary: 销售订单字段
- source: `../../sources/pages/api-3478253.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/order/info

- operationId: `get_v1_invoices_order_info`
- summary: 销售订单详情
- source: `../../sources/pages/api-3478251.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | order_id      | integer | no       | 销售订单ID或销售订单编号必须传其中一个                     |
| query  | order_no      | string  | no       | 销售订单ID或销售订单编号必须传其中一个                     |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/order/list

- operationId: `get_v1_invoices_order_list`
- summary: 销售订单列表
- source: `../../sources/pages/api-3478254.md`

### parameters

| in     | name                | type    | required | description                                                        |
| ------ | ------------------- | ------- | -------- | ------------------------------------------------------------------ |
| query  | start_time          | string  | no       | 开始时间，YYYY-MM-DD                                                    |
| query  | end_time            | string  | no       | 结束时间，YYYY-MM-DD                                                    |
| query  | time_type           | integer | no       | 控制start_time，end_time查询什么时间字段，默认值=1，1 更新时间 , 2 创建时间，3 订单日期，4 删除时间  |
| query  | count               | integer | no       | 每页数量，默认10                                                          |
| query  | start_index         | integer | no       | 页码，默认1                                                             |
| query  | removed             | integer | no       | 是否返回已经删除订单，1是返回已经删除订单                                              |
| query  | approval            | integer | no       | 审核状态，1是有审批                                                         |
| query  | approval_with_draft | integer | no       | 查询的已审核单据是否包含草稿：1-是，0-否。默认值为 0                                      |
| query  | status              | integer | no       | 订单状态，传入值来自/v1/invoices/order/orderEnums返回值中order_status_list中的code |
| header | Authorization       | string  | yes      | 从/v1/oauth2/access_token获取到的access_token                           |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/order/orderEnums

- operationId: `get_v1_invoices_order_orderenums`
- summary: 销售订单枚举:货币，付款方式，国家/地区，订单类型，订单状态，订单创建方式
- source: `../../sources/pages/api-3485287.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/invoices/order/push

- operationId: `post_v1_invoices_order_push`
- summary: 销售订单新建/编辑
- source: `../../sources/pages/api-3478252.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                      | type         | required | description                                                                                           |
| ------------------------- | ------------ | -------- | ----------------------------------------------------------------------------------------------------- |
| 12345677                  | array        | no       | 12345677为例子，自定义字段可以从【销售订单字段】接口中查到字段ID，若自定义多选字段，数组传入，值来自/v1/invoices/order/fields中对应字段的ext_info中的一个或多个 |
| 12345678                  | string       | no       | 12345678为例子，自定义字段可以从【销售订单字段】接口中查到字段ID，若自定义单选字段，值来自/v1/invoices/order/fields中对应字段的ext_info中的一个         |
| order_id                  | integer      | no       | 订单ID，编辑时可以传入订单ID或者订单编号                                                                                |
| order_no                  | string       | no       | 订单编号，编辑时可以传入订单ID或者订单编号                                                                                |
| account_date              | string       | no       | 订单日期，YYYY-mm-dd                                                                                       |
| name                      | string       | no       | 订单名称                                                                                                  |
| exchange_rate             | number/float | no       | 折现人民币汇率，exchange_rate不传入时默认取当前系统设置的汇率，这里有传币种，不传exchange_rate的话就会exchange_rate和exhange_rate_usd都取系统实时  |
| exchange_rate_usd         | number/float | no       | 折现美元汇率，exchange_rate不传入时默认取当前系统实时的汇率                                                                  |
| currency                  | string       | yes      | 币种，传入值来自/v1/invoices/order/orderEnums返回值中currency_list的code                                           |
| amount                    | number/float | no       | 订单金额                                                                                                  |
| amount_rmb                | number/float | no       | 订单金额（人民币）                                                                                             |
| amount_usd                | number/float | no       | 订单金额（美元）                                                                                              |
| addition_cost_amount      | number/float | no       | 附加费用总金额                                                                                               |
| product_total_amount      | number/float | no       | 产品总金额                                                                                                 |
| product_total_count       | integer      | no       | 产品总数量                                                                                                 |
| price_contract            | string       | no       | 价格条款,参考说明中的价格条款枚举值                                                                                    |
| receive_remittance_way    | string       | no       | 付款方式，传入值来自/v1/invoices/order/orderEnums返回值中pay_list的code                                              |
| price_contract_remark     | string       | no       | 价格条款说明                                                                                                |
| receive_remittance_remark | string       | no       | 收汇方式说明                                                                                                |
| insurance_remark          | string       | no       | 保险说明                                                                                                  |
| order_contract            | string       | no       | 订单条款                                                                                                  |
| company_id                | integer      | no       | 客户ID，请从客户列表中获取客户ID传入                                                                                  |
| company_name              | string       | no       | 客户名称                                                                                                  |
| company_phone             | string       | no       | 客户电话                                                                                                  |
| company_fax               | string       | no       | 客户传真                                                                                                  |
| company_address           | string       | no       | 客户地址                                                                                                  |
| country                   | string       | no       | 国家/地区:ISO两位编码                                                                                         |
| opportunity_id            | integer      | no       | 商机id，请从商机列表等中拿到商机ID传入                                                                                 |
| shipment_deadline_remark  | string       | no       | 交货期                                                                                                   |
| users                     | array        | no       | 业绩归属人                                                                                                 |
| product_list              | array        | no       | 产品子列表                                                                                                 |
| customer_name             | string       | no       | 联系人名称                                                                                                 |
| customer_phone            | string       | no       | 联系人电话                                                                                                 |
| customer_email            | string       | no       | 联系人邮箱                                                                                                 |
| customer_address          | string       | no       | 联系人地址                                                                                                 |
| transport_mode            | string       | no       | 运输方式，值为 空运、海运、陆运、邮政、快递、其他                                                                             |
| shipment_deadline         | string       | no       | 装运期限                                                                                                  |
| shipment_port             | string       | no       | 装运港口                                                                                                  |
| target_port               | string       | no       | 目的港口                                                                                                  |
| more_or_less              | string       | no       | 溢短装                                                                                                   |
| package_remark            | string       | no       | 包装说明                                                                                                  |
| marked                    | string       | no       | 唛头                                                                                                    |
| create_user               | integer      | no       | 创建人，传入值来自/v1/user/list中的user_id                                                                       |
| create_time               | string       | no       | 创建时间                                                                                                  |
| remark                    | integer      | no       | 备注                                                                                                    |
| source_type               | integer      | no       | 订单类型：1 CRM订单，默认1，传入值来自/v1/invoices/order/orderEnums返回值中source_type_list的code                          |
| status                    | integer      | no       | 订单状态，传入值来自/v1/invoices/order/orderEnums返回值中order_status_list中的code                                    |
| tax_refund_type           | integer      | no       | 是否退税，1不退税，2退税，默认0                                                                                     |
| customer_id               | integer      | no       | 联系人ID，请从客户列表或者客户联系人列表中获取联系人ID传入                                                                       |
| cost_list                 | array        | no       | 费用                                                                                                    |
| file_list                 | array        | no       | 附件，数组传入，完整可以访问的文件链接                                                                                   |
| capital_account_id        | integer      | no       | 资金账号ID，值来自/v1/capitalAccount/list的capital_account_id                                                  |
| departments               | array        | no       | 业绩归属部门                                                                                                |
| handler                   | array        | no       | 处理人，数组传入，传入值来自/v1/user/list中的user_id                                                                  |
| user_id                   | integer      | no       | 当前操作用户                                                                                                |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/order/remove

- operationId: `post_v1_invoices_order_remove`
- summary: 销售订单删除
- source: `../../sources/pages/api-3478257.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | order_id      | integer | no       | 销售订单ID，销售订单ID或销售订单编号必须传其中一个              |
| query  | order_no      | string  | no       | 销售订单编号，销售订单ID或销售订单编号必须传其中一个              |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
