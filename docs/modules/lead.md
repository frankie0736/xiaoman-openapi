# 线索

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/lead.openapi.yaml`
- endpoints: `4`

## GET /v1/lead/fields

- operationId: `get_v1_lead_fields`
- summary: 线索|联系人的数据字典
- source: `../../sources/pages/api-3484687.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| query  | type          | string | no       | lead=线索数据字典，customer=联系人数据字典 默认值: lead   |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/lead/info

- operationId: `get_v1_lead_info`
- summary: 线索数据查询
- source: `../../sources/pages/api-3484689.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | lead_id       | integer | no       | 线索ID 值来源于/v1/lead/list                   |
| query  | serial_id     | string  | no       | 线索编号                                     |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/lead/list

- operationId: `get_v1_lead_list`
- summary: 线索列表
- source: `../../sources/pages/api-3484688.md`

### parameters

| in     | name          | type    | required | description                                               |
| ------ | ------------- | ------- | -------- | --------------------------------------------------------- |
| query  | start_index   | integer | no       | 第几页，默认 = 1                                                |
| query  | count         | integer | no       | 每页记录数，默认 = 10                                             |
| query  | start_time    | string  | no       | 时间查询范围：开始日期                                               |
| query  | end_time      | string  | no       | 时间查询范围：结束日期                                               |
| query  | email         | string  | no       | 联系人邮箱                                                     |
| query  | origin        | integer | no       | 线索来源 值来源于接口/v1/company/fields/selector                    |
| query  | sort_field    | string  | no       | 排序与搜索字段 update_time 默认值 order_time最近联系时间 edit_time 最近编辑时间 |
| query  | archive       | integer | no       | 归档状态 1:已归档 2:已转化                                          |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token                  |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/lead/push

- operationId: `post_v1_lead_push`
- summary: 线索（含联系人）创建/编辑接口
- source: `../../sources/pages/api-3478299.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name         | type    | required | description                                      |
| ------------ | ------- | -------- | ------------------------------------------------ |
| user_id      | integer | no       | 不填则默认为创建人 值来自于/v1/user/list接口                    |
| name         | string  | yes      |                                                  |
| country      | string  | no       | 非必填,ISO两位码                                       |
| province     | string  | no       | 对接需要询问对接协助开发获取省枚举                                |
| city         | string  | no       | 对接需要询问对接协助开发获取市枚举                                |
| tel          | string  | no       |                                                  |
| fax          | string  | no       |                                                  |
| biz_type     | integer | no       | 可选字段 /v1/company/companyEnums                    |
| address      | string  | no       | 可选字段                                             |
| remark       | string  | no       | 可选字段                                             |
| homepage     | string  | no       | 可选字段                                             |
| customers    | array   | no       |                                                  |
| lead_id      | integer | no       | 编辑时需要设置 值来自于/v1/lead/list接口                      |
| origin_list  | array   | no       | 可选字段，从v1/company/fields/selector?field=origin选择  |
| company_name | string  | no       |                                                  |
| short_name   | string  | no       |                                                  |
| scale_id     | integer | no       | 值来自/v1/company/companyEnums 接口                   |
| group_id     | integer | no       | 从分组v1/company/fields/selector?field=group_id选择   |
| status       | integer | no       | 可选字段：1=>待处理,2=>无效,3=>完善信息,4=>初步触达,5=>联系互动,7=>已转化 |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
