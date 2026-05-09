# 报价单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/quotation.openapi.yaml`
- endpoints: `6`

## GET /v1/invoices/quotation/fields

- operationId: `get_v1_invoices_quotation_fields`
- summary: 报价单数据字典
- source: `../../sources/pages/api-3478281.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/invoices/quotation/fields/selector

- operationId: `get_v1_invoices_quotation_fields_selector`
- summary: 报价单状态、币种查询
- source: `../../sources/pages/api-3480193.md`

### parameters

| in     | name          | type   | required | description                                   |
| ------ | ------------- | ------ | -------- | --------------------------------------------- |
| query  | field         | string | no       | 查询字段值，field=status,报价单状态；field=currency,报价单币种 |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token      |

### responses

| status          | contentTypes     | description |
| --------------- | ---------------- | ----------- |
| 200             | application/json |             |
| x-200:请求成功      | application/json |             |
| x-200:查询报价单状态成功 | application/json |             |
| x-200:查询报价单币种成功 | application/json |             |

## GET /v1/invoices/quotation/info

- operationId: `get_v1_invoices_quotation_info`
- summary: 查询报价单详情
- source: `../../sources/pages/api-3478282.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name         | type   | required | description |
| ------------ | ------ | -------- | ----------- |
| quotation_id | string | yes      |             |
| quotation_no | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
| 404    | application/json |             |

## GET /v1/invoices/quotation/list

- operationId: `get_v1_invoices_quotation_list`
- summary: 报价单列表
- source: `../../sources/pages/api-3480192.md`

### parameters

| in     | name          | type   | required | description                                  |
| ------ | ------------- | ------ | -------- | -------------------------------------------- |
| query  | start_time    | string | no       | 时间查询范围：开始日期                                  |
| query  | end_time	     | string | no       | 时间查询范围：结束日期                                  |
| query  | start_index   | number | no       | 第几页，默认 = 1                                   |
| query  | count         | number | no       | 每页记录数，默认 = 10                                |
| query  | removed       | number | no       | 默认0，1表示查询已删除的数据列表                            |
| query  | approval      | number | no       | 默认0，1表示查询审批通过的数据列表                           |
| query  | status        | string | no       | 默认值: 0，设置对应的状态值可以查询相关状态的数据列表，支持以半角逗号分割的多个状态值 |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token     |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/invoices/quotation/push

- operationId: `post_v1_invoices_quotation_push`
- summary: 报价单新建/编辑
- source: `../../sources/pages/api-3478280.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name           | type    | required | description                          |
| -------------- | ------- | -------- | ------------------------------------ |
| 40444081       | string  | yes      | 数字类型字段ID是用户的自定义字段，请参考fields接口返回的字段列表 |
| quotation_id   | integer | no       | 提供quotation_id可以修改旧报价单数据             |
| name           | string  | yes      | 报价单名称                                |
| company_name   | string  | yes      | 报价单关联客户名称                            |
| user_id        | integer | yes      | 小满用户UserID                           |
| company_id     | integer | yes      | 小满客户ID                               |
| remark         | string  | yes      | 备注                                   |
| currency       | string  | yes      | 币种                                   |
| quotation_date | string  | yes      | 报价日期                                 |
| product_list   | array   | yes      |                                      |
| quotation_no   | string  | no       | 报价单编号                                |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/invoices/quotation/remove

- operationId: `post_v1_invoices_quotation_remove`
- summary: 报价单删除
- source: `../../sources/pages/api-3480194.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

| name         | type   | required | description                                     |
| ------------ | ------ | -------- | ----------------------------------------------- |
| quotation_id | number | no       | 报价单ID，可以从报价单列表接口[/v1/invoices/quotation/list]获得 |
| quotation_no | string | no       | 报价单编号                                           |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
