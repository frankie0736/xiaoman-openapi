# 费用单

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/cost-invoice.openapi.yaml`
- endpoints: `4`

## GET /v1/costInvoice/fields

- operationId: `get_v1_costinvoice_fields`
- summary: 费用单字段
- source: `../../sources/pages/api-3483961.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/costInvoice/info

- operationId: `get_v1_costinvoice_info`
- summary: 费用单-详情
- source: `../../sources/pages/api-3483958.md`

### parameters

| in     | name            | type    | required | description                              |
| ------ | --------------- | ------- | -------- | ---------------------------------------- |
| query  | cost_invoice_no | string  | no       | 费用单编号 编号和ID必须填写一项                        |
| query  | cost_invoice_id | integer | no       | 费用单ID                                    |
| header | Authorization   | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/costInvoice/items

- operationId: `get_v1_costinvoice_items`
- summary: 费用项目列表
- source: `../../sources/pages/api-3484020.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/costInvoice/list

- operationId: `get_v1_costinvoice_list`
- summary: 费用单列表
- source: `../../sources/pages/api-3484720.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | time_type     | integer | no       | 时间筛选 1-按更新时间，2-按创建时间                     |
| query  | start_time    | string  | no       | 开始时间                                     |
| query  | end_time      | string  | no       | 截止时间                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | count         | integer | no       | 每页数量                                     |
| query  | removed       | integer | no       | 默认值: 0，设置=1时查询已删除的数据列表                   |
| query  | status        | integer | no       | 费用单状态:1-待审批、2-待付款、3-部分付款、4-已结清           |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
