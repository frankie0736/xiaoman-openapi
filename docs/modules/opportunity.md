# 商机

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/opportunity.openapi.yaml`
- endpoints: `6`

## GET /v1/opportunity/fields

- operationId: `get_v1_opportunity_fields`
- summary: 商机数据字典
- source: `../../sources/pages/api-3478288.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/opportunity/fields/selector

- operationId: `get_v1_opportunity_fields_selector`
- summary: 查询商机的销售流程 商机阶段 输单原因
- source: `../../sources/pages/api-3485300.md`

### parameters

| in     | name          | type    | required | description                                          |
| ------ | ------------- | ------- | -------- | ---------------------------------------------------- |
| query  | field         | integer | no       | 销售流程:sales_flow 销售阶段:stage_list 输单原因fail_reason      |
| query  | flow_id       | integer | no       | 销售流程ID ：查询销售阶段时候需要带上销售流程ID，数据来源于当前接口field=sales_flow |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token             |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/opportunity/info

- operationId: `get_v1_opportunity_info`
- summary: 商机数据查询
- source: `../../sources/pages/api-3478287.md`

### parameters

| in     | name           | type    | required | description                     |
| ------ | -------------- | ------- | -------- | ------------------------------- |
| query  | opportunity_id | integer | no       | 商机ID 值来自/v1/opportunity/list 接口 |
| query  | serial_id      | string  | no       | 商机编号                            |
| header | Authorization  | string  | yes      |                                 |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/opportunity/list

- operationId: `get_v1_opportunity_list`
- summary: 商机列表
- source: `../../sources/pages/api-3478286.md`

### parameters

| in     | name          | type    | required | description   |
| ------ | ------------- | ------- | -------- | ------------- |
| query  | start_index   | integer | no       | 第几页，默认 = 1    |
| query  | count         | integer | no       | 每页记录数，默认 = 10 |
| query  | start_time    | string  | no       | 更新时间查询范围：开始日期 |
| query  | end_time      | string  | no       | 更新时间查询范围：结束日期 |
| header | Authorization | string  | yes      |               |

### requestBody
- contentType: `multipart/form-data` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/opportunity/push

- operationId: `post_v1_opportunity_push`
- summary: 商机新建/编辑接口
- source: `../../sources/pages/api-3478289.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name              | type    | required | description                            |
| ----------------- | ------- | -------- | -------------------------------------- |
| opportunity_id    | integer | no       | 编辑时必填 值来自/v1/opportunity/list 接口       |
| name              | string  | yes      |                                        |
| amount            | string  | no       |                                        |
| exchange_rate     | string  | no       |                                        |
| exchange_rate_usd | string  | no       |                                        |
| account_date      | string  | no       |                                        |
| stage             | integer | no       | 值来自于/v1/opportunity/fields/selector 接口 |
| currency          | string  | no       |                                        |
| company_id        | integer | yes      | 新建时必填 值来自/v1/company/list 接口           |
| customer_id       | array   | no       |                                        |
| origin_list       | array   | no       |                                        |
| fail_type         | integer | no       | 值来自于/v1/opportunity/fields/selector 接口 |
| fail_remark       | string  | no       |                                        |
| handler           | array   | yes      | 值来自于/v1/user/list 接口                   |
| main_user         | integer | no       |                                        |
| flow_id           | number  | no       | 值来自于/v1/opportunity/fields/selector 接口 |
| busines_type_id   | number  | yes      |                                        |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/opportunity/remove

- operationId: `post_v1_opportunity_remove`
- summary: 商机删除接口
- source: `../../sources/pages/api-3485301.md`

### parameters

| in     | name           | type    | required | description                              |
| ------ | -------------- | ------- | -------- | ---------------------------------------- |
| query  | opportunity_id | integer | yes      | 商机ID 值来自于/v1/opportunity/list 商机列表接口     |
| header | Authorization  | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
