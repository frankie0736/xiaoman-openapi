# 供应商

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/supplier.openapi.yaml`
- endpoints: `6`

## GET /v1/supplier/fields

- operationId: `get_v1_supplier_fields`
- summary: 供应商字段
- source: `../../sources/pages/api-3481699.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/supplier/info

- operationId: `get_v1_supplier_info`
- summary: 供应商详情
- source: `../../sources/pages/api-3478283.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | supplier_id   | integer | yes      | 供应商ID                                    |
| query  | supplier_name | string  | no       | 供应商名称                                    |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/supplier/list

- operationId: `get_v1_supplier_list`
- summary: 供应商列表
- source: `../../sources/pages/api-3481691.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | start_time    | string  | no       | 更新开始时间                                   |
| query  | end_time      | string  | no       | 更新截止时间                                   |
| query  | count         | integer | no       | 每页数量                                     |
| query  | start_index   | integer | no       | 页码                                       |
| query  | is_delete     | integer | no       | 默认值: 0，设置=1时查询已删除的数据列表                   |
| query  | page_size     | integer | yes      |                                          |
| query  | page_no       | integer | yes      |                                          |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/supplier/push

- operationId: `post_v1_supplier_push`
- summary: 供应商新增/编辑
- source: `../../sources/pages/api-3478285.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name          | type    | required | description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| 3137211747    | string  | no       | 供应商自定义字段。字段名称为/v1/supplier/fields 获取到的自定义字段ID             |
| supplier_id   | integer | no       | 供应商ID，编辑时传递                                               |
| name          | string  | yes      | 供应商名称，必填                                                  |
| archive_user  | integer | no       | 创建人，不填默认为主账号                                              |
| rate_id       | integer | no       | 供应商评级，非必填，crm是枚举，接口补充中~~                                  |
| homepage      | string  | no       | 公司网址，非必填                                                  |
| address       | string  | no       | 供应商地址，非必填                                                 |
| remark        | string  | no       | 备注，非必填                                                    |
| delivery_date | integer | no       | 参考交期，非必填，crm是枚举,1：1-2天；2: 3-5天；3：5-10天 4: 10-15天，5: > 15天 |
| contact_list  | array   | no       | 联系人列表，没有则不传，或者空数组                                         |
| supplier_no   | string  | no       | 供应商编号                                                     |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/supplier/remove

- operationId: `post_v1_supplier_remove`
- summary: 供应商删除
- source: `../../sources/pages/api-3484731.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | supplier_id   | integer | yes      | 供应商ID                                    |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/supplierProduct/supplierProductRelationList

- operationId: `get_v1_supplierproduct_supplierproductrelationlist`
- summary: 获取供应商产品列表
- source: `../../sources/pages/api-3498455.md`

### parameters

| in     | name                  | type   | required | description                              |
| ------ | --------------------- | ------ | -------- | ---------------------------------------- |
| query  | product_no            | string | no       |                                          |
| query  | supplier_product_no   | string | no       |                                          |
| query  | product_id            | string | no       |                                          |
| query  | suku_id               | string | no       |                                          |
| query  | supplier_id           | string | no       |                                          |
| query  | supplier_product_name | string | no       |                                          |
| header | Authorization         | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
