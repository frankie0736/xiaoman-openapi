# 库存

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/warehouse.openapi.yaml`
- endpoints: `2`

## POST /v1/product/push-inventory

- operationId: `post_v1_product_push_inventory`
- summary: 库存写入
- source: `../../sources/pages/api-3478297.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `array`

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/warehouse/list

- operationId: `get_v1_warehouse_list`
- summary: 仓库查询
- source: `../../sources/pages/api-3478298.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | warehouse_id  | integer | no       | 仓库ID查询条件                                 |
| query  | warehouse_no  | string  | no       | 仓库编号                                     |
| header | authorization | string  | yes      |                                          |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
