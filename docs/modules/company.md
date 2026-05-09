# 客户

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/company.openapi.yaml`
- endpoints: `17`

## GET /v1/company/companyEnums

- operationId: `get_v1_company_companyenums`
- summary: 客户枚举:客户类型，客户标签，时区，规模，星级，采购意向，采购额度，职级
- source: `../../sources/pages/api-3484706.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/company/fields

- operationId: `get_v1_company_fields`
- summary: 客户数据字典
- source: `../../sources/pages/api-3478270.md`

### parameters

| in     | name          | type   | required | description                                  |
| ------ | ------------- | ------ | -------- | -------------------------------------------- |
| query  | type          | string | no       | company=客户数据字典，customer=联系人数据字典 默认值: company |
| header | Authorization | string | yes      |                                              |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/company/fields/selector

- operationId: `get_v1_company_fields_selector`
- summary: 查询客户的阶段、分组、状态、地区、主营产品、来源
- source: `../../sources/pages/api-3478275.md`

### parameters

| in     | name          | type   | required | description                                                                                                                                           |
| ------ | ------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| query  | field         | string | no       | 可传的值，field=trail_status，客户阶段；field=group_id，客户分组；field=pool_id，公海分组；field=origin,来源列表；field=product_group，产品分组；field=category，主营产品；field=country，国家地区 |
| header | Authorization | string | yes      |                                                                                                                                                       |

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/company/info

- operationId: `get_v1_company_info`
- summary: 客户详情
- source: `../../sources/pages/api-3473043.md`

### parameters

| in     | name          | type    | required | description                            |
| ------ | ------------- | ------- | -------- | -------------------------------------- |
| query  | company_id    | integer | no       | 公司客户ID 来自于/v1/company/list接口company_id |
| query  | format        | string  | no       | 是否返回格式化后的数据，默认值: 0                     |
| query  | serial_id     | string  | no       | 客户编号 来自于/v1/company/list接口serial_id    |
| header | Authorization | string  | yes      |                                        |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/company/list

- operationId: `get_v1_company_list`
- summary: 客户列表
- source: `../../sources/pages/api-3480070.md`

### parameters

| in     | name          | type    | required | description                                                                     |
| ------ | ------------- | ------- | -------- | ------------------------------------------------------------------------------- |
| query  | count         | integer | no       | 每页数量                                                                            |
| query  | start_index   | integer | no       | 页码                                                                              |
| query  | removed       | string  | no       | 默认值:0，设置=1时查询已删除的数据列表                                                           |
| query  | all           | string  | no       | 默认值:1，设置=1查询所有客户，设置=0只查询私海客户，设置=2查询公海客户                                         |
| query  | group_id      | integer | no       | 设置客户分组ID后，只查询对应分组的客户 传入值来自/v1/company/fields/selector?field=group_id返回值data中的id |
| query  | start_time    | string  | no       | 开始时间，YYYY-MM-DD                                                                 |
| query  | end_time      | string  | no       | 结束时间，YYYY-MM-DD                                                                 |
| query  | time_type     | string  | no       | 控制start_time，end_time查询什么时间字段，默认值=1，1 更新时间 , 2 创建时间, 3 建档时间                     |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token                                        |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/moveToPublic

- operationId: `post_v1_company_movetopublic`
- summary: 移入公海
- source: `../../sources/pages/api-3496722.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |
| header | Content-Type  | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name             | type    | required | description |
| ---------------- | ------- | -------- | ----------- |
| company_id       | integer | yes      |             |
| user_id          | integer | no       |             |
| public_reason_id | integer | no       |             |
| pool_id          | integer | no       |             |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/push/customer

- operationId: `post_v1_company_push_customer`
- summary: 新增客户的联系人（待修改）
- source: `../../sources/pages/api-3484681.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name          | type    | required | description |
| ------------- | ------- | -------- | ----------- |
| company_id    | integer | no       | 客户ID        |
| serial_id     | string  | no       | 客户编号        |
| name          | string  | no       | 联系人名称       |
| tel_area_code | string  | no       | 联系人电话区号     |
| tel           | string  | no       | 联系人电话号码     |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/pushCompanyAndCustomers

- operationId: `post_v1_company_pushcompanyandcustomers`
- summary: 客户（含联系人）新增/编辑
- source: `../../sources/pages/api-3478272.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name                | type    | required | description                                                                                                                                    |
| ------------------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| company_id          | integer | no       | 编辑时需要设置 值来自于/v1/company/list接口                                                                                                                 |
| user_id             | integer | no       | 不填则默认为创建人 值来自于/v1/user/list接口                                                                                                                  |
| batch_user_ids      | array   | no       | eg: [11, 22] 值来自于/v1/user/list接口                                                                                                               |
| remove_user_id      | array   | no       | eg: [33, 44] 值来自于/v1/user/list接口                                                                                                               |
| is_public           | integer | no       | 私海客户is_public=0;公海客户is_public=1;默认is_public=0                                                                                                  |
| serial_id           | string  | no       | 可选字段,不设置默认生成                                                                                                                                   |
| name                | string  | yes      |                                                                                                                                                |
| short_name          | string  | no       |                                                                                                                                                |
| country             | string  | no       | 非必填,ISO两位码                                                                                                                                     |
| province            | string  | no       | 对接需要询问对接协助开发获取省枚举                                                                                                                              |
| city                | string  | no       | 对接需要询问对接协助开发获取市枚举                                                                                                                              |
| tel_area_code       | string  | no       |                                                                                                                                                |
| tel                 | string  | no       |                                                                                                                                                |
| fax                 | string  | no       |                                                                                                                                                |
| group_id            | integer | no       | 可选字段,从分组v1/company/fields/selector?field=group_id选择                                                                                            |
| pool_id             | integer | no       | 必填,不确定可设置为0,代表未分组，从v1/company/fields/selector?field=pool_id选择                                                                                  |
| trail_status        | integer | no       | 可选字段,从v1/company/fields/selector?field=trail_status选择                                                                                          |
| biz_type            | integer | no       | 可选字段 值来自/v1/company/companyEnums接口                                                                                                             |
| cus_tag             | array   | no       | 非必填 值来自/v1/company/companyEnums接口                                                                                                              |
| address             | string  | no       | 可选字段                                                                                                                                           |
| remark              | string  | no       | 可选字段                                                                                                                                           |
| homepage            | string  | no       | 可选字段                                                                                                                                           |
| star                | integer | no       | 可选字段，1-5之间                                                                                                                                     |
| intention_level     | integer | no       | 0未知，1低，2中，3高                                                                                                                                   |
| annual_procurement  | integer | no       | 0: 无采购额 1: 0~1千美元 2: 1千～5千美元 3: 5千～1万美元 4: 1万～3万美元 5: 3万～5万美元 6: 5万～10万美元 7: 10万～30万美元 8: 30万～50万美元 9: 50万～100万美元 10: 100万～500万美元 11: 500万美元以上 |
| timezone            | integer | no       | 非必填                                                                                                                                            |
| scale_id            | integer | no       | 1：少于59人,2：60-149人,3：150-499人,4：500-999人,5：1000-4999人，6: 5000人以上                                                                                |
| image_list          | array   | no       | 非必填，example: ['xx1', 'xx2'], 需要传可访问的URL                                                                                                        |
| next_follow_up_time | string  | no       | 非必填                                                                                                                                            |
| category_ids        | array   | no       | 非必填，example: [[1, 2, 3], [4, 5, 6]]                                                                                                            |
| product_group_ids   | array   | no       | 非必填，example: [1, 2]                                                                                                                            |
| customers           | array   | yes      |                                                                                                                                                |
| origin_list         | array   | no       | 可选字段，从v1/company/fields/selector?field=origin选择                                                                                                |
| refresh_user_id     | boolean | no       | batch_user_ids不为空时才生效，当true时触发重新分配，false则为共享                                                                                                   |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/company/pushGroup

- operationId: `post_v1_company_pushgroup`
- summary: 客户分组新增/编辑
- source: `../../sources/pages/api-3484700.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name       | type    | required | description                                                         |
| ---------- | ------- | -------- | ------------------------------------------------------------------- |
| group_id   | integer | no       | 编辑时候需要传递 传入值来自/v1/company/fields/selector?field=group_id返回值data中的id |
| group_name | string  | yes      | 客户分组名称                                                              |
| parent_id  | integer | no       | 客户分组父级ID                                                            |
| owner_ids  | string  | no       | 客户分组可用成员，用户ID列表 数据来自/v1/user/list接口中data下面的user_id                  |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/pushTag

- operationId: `post_v1_company_pushtag`
- summary: 客户标签新增/编辑
- source: `../../sources/pages/api-3484704.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name      | type    | required | description                                             |
| --------- | ------- | -------- | ------------------------------------------------------- |
| tag_id    | integer | no       | 客户标签ID，编辑时必填 传入值来自/v1/company/companyEnums返回值中的tag_list |
| tag_name  | string  | yes      | 客户标签名称，必填                                               |
| tag_color | string  | no       | 客户标签颜色，非必填，例子#188ae8                                    |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/pushTrail

- operationId: `post_v1_company_pushtrail`
- summary: 客户阶段新增/编辑
- source: `../../sources/pages/api-3484702.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name        | type    | required | description                                      |
| ----------- | ------- | -------- | ------------------------------------------------ |
| trail_id    | integer | no       | 客户阶段ID，编辑时必填 传入值来自/v1/company/fields/selector返回值 |
| trail_name  | string  | yes      | 客户阶段名称，必填                                        |
| trail_color | string  | no       | 客户阶段颜色，非必填，例子#188ae8                             |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/removeCompanyAndCustomers

- operationId: `post_v1_company_removecompanyandcustomers`
- summary: 删除客户（仅支持公海客户）
- source: `../../sources/pages/api-3478274.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

| name       | type    | required | description                 |
| ---------- | ------- | -------- | --------------------------- |
| company_id | integer | yes      | 客户ID 值来自于/v1/company/list接口 |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/company/removeGroup

- operationId: `post_v1_company_removegroup`
- summary: 删除客户分组
- source: `../../sources/pages/api-3484701.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `multipart/form-data` schema: `object`

| name     | type    | required | description                                               |
| -------- | ------- | -------- | --------------------------------------------------------- |
| group_id | integer | yes      | 客户分组ID 传入值来自/v1/company/fields/selector?field=group_id返回值 |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/removeTag

- operationId: `post_v1_company_removetag`
- summary: 删除客户标签
- source: `../../sources/pages/api-3484705.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `multipart/form-data` schema: `object`

| name   | type    | required | description                                       |
| ------ | ------- | -------- | ------------------------------------------------- |
| tag_id | integer | yes      | 客户标签ID 传入值来自/v1/company/companyEnums返回值中的tag_list |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/company/removeTrail

- operationId: `post_v1_company_removetrail`
- summary: 删除客户阶段
- source: `../../sources/pages/api-3484703.md`

### parameters

| in     | name          | type    | required | description                                                |
| ------ | ------------- | ------- | -------- | ---------------------------------------------------------- |
| query  | trail_id      | integer | yes      | 客户阶段ID 传入值来自/v1/company/fields/selector返回值                 |
| query  | to_trail_id   | integer | yes      | 被删除客户阶段若有应用被前往这个客户阶段ID 传入值来自/v1/company/fields/selector返回值 |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token                   |

### requestBody
- contentType: `multipart/form-data` schema: `object`

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/dynamic/trail/list

- operationId: `get_v1_dynamic_trail_list`
- summary: 跟进动态查询接口
- source: `../../sources/pages/api-3478244.md`

### parameters

| in     | name           | type    | required | description                              |
| ------ | -------------- | ------- | -------- | ---------------------------------------- |
| query  | company_id     | integer | no       | 客户ID                                     |
| query  | lead_id        | integer | no       | 线索ID                                     |
| query  | opportunity_id | integer | no       | 商机ID                                     |
| query  | start_time     | string  | no       | 开始时间                                     |
| query  | end_time       | string  | no       | 结束时间                                     |
| query  | count          | integer | no       | 每页数量                                     |
| query  | start_index    | integer | no       | 页码                                       |
| header | Authorization  | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/dynamic/trail/push

- operationId: `post_v1_dynamic_trail_push`
- summary: 提交跟进动态
- source: `../../sources/pages/api-3484682.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name           | type    | required | description                                                                                                            |
| -------------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| company_id     | integer | no       | 客户ID                                                                                                                   |
| lead_id        | integer | no       | 线索ID                                                                                                                   |
| content        | string  | no       | 动态内容                                                                                                                   |
| remark_type    | integer | no       | 跟进动态类型 默认101 101:快速记录 102:关联邮件备注 103:电话 104:会面 105:社交平台 106:总部拜访 107:办事处拜访 108:来访总部 109:来访办事处 110:邮件 111:客户拜访 112:日程跟进 |
| opportunity_id | integer | no       | 商机ID                                                                                                                   |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
