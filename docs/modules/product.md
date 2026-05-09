# 产品

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/product.openapi.yaml`
- endpoints: `15`

## POST /v1/product/append-sku-attributes-value

- operationId: `post_v1_product_append_sku_attributes_value`
- summary: 增量更新产品规格值
- source: `../../sources/pages/api-3489012.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name       | type    | required | description                         |
| ---------- | ------- | -------- | ----------------------------------- |
| item_id    | integer | yes      | 值来自接口/v1/product/sku-attribute-list |
| attributes | array   | yes      |                                     |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/product/edit-parts-list

- operationId: `post_v1_product_edit_parts_list`
- summary: 产品配件新建/编辑
- source: `../../sources/pages/api-3501059.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name       | type    | required | description       |
| ---------- | ------- | -------- | ----------------- |
| sku_id     | integer | yes      | 需要添加配件的主产品的sku_id |
| parts_list | array   | yes      | 配件列表              |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/product/fields

- operationId: `get_v1_product_fields`
- summary: 产品库的数据字典
- source: `../../sources/pages/api-3478262.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/product/groups

- operationId: `get_v1_product_groups`
- summary: 查询产品分组
- source: `../../sources/pages/api-3478266.md`

### parameters

| in     | name          | type   | required | description        |
| ------ | ------------- | ------ | -------- | ------------------ |
| query  | group_id      | string | no       | 产品分组ID 不传则查询所有产品分组 |
| query  | group_name    | string | no       | 产品分组名称             |
| header | Authorization | string | yes      |                    |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/product/info

- operationId: `get_v1_product_info`
- summary: 产品详情
- source: `../../sources/pages/api-3478263.md`

### parameters

| in     | name          | type    | required | description            |
| ------ | ------------- | ------- | -------- | ---------------------- |
| query  | product_no    | string  | no       | 产品编码，最长256个字符          |
| query  | product_id    | integer | no       | 产品ID，与上product_no参数二选一 |
| header | Authorization | string  | yes      |                        |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
| 404    | application/json |             |

## GET /v1/product/inventory-list

- operationId: `get_v1_product_inventory_list`
- summary: 库存查询(通过skuId) 
- source: `../../sources/pages/api-3485273.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| query  | sku_id        | string | no       | SKU ID 多个之间使用逗号隔开                        |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/product/list

- operationId: `get_v1_product_list`
- summary: 查询产品库列表
- source: `../../sources/pages/api-3478259.md`

### parameters

| in     | name          | type    | required | description           |
| ------ | ------------- | ------- | -------- | --------------------- |
| query  | time_type     | integer | no       | 时间筛选 1-按更新时间，2-按创建时间  |
| query  | start_time    | string  | no       | 开始时间                  |
| query  | end_time      | string  | no       | 截止时间                  |
| query  | start_index   | integer | no       | 页码                    |
| query  | count         | integer | no       | 每页数量                  |
| query  | product_type  | integer | no       | 产品类型 1:无规格 2:多规格 3:组合 |
| header | Authorization | string  | yes      |                       |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/product/productEnums

- operationId: `get_v1_product_productenums`
- summary: 产品枚举:产品类型，离岸价设置类型，创建方式，产品计量单位 
- source: `../../sources/pages/api-3484723.md`

### parameters

| in     | name          | type   | required | description                                                                           |
| ------ | ------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| query  | field         | string | yes      | unit_list :返回计量单位 product_type_ist:返回产品类型 fob_type_ist:返回离岸价类型 source_type_ist:返回创建方式 |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token                                              |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/product/push

- operationId: `post_v1_product_push`
- summary: 产品新建/编辑
- source: `../../sources/pages/api-3478260.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `application/json` schema: `object`

| name                  | type         | required | description         |
| --------------------- | ------------ | -------- | ------------------- |
| product_id            | integer      | no       | 编辑时必填               |
| product_no            | string       | no       | 最长256个字符            |
| name                  | string       | no       | 最长256个字符            |
| cn_name               | string       | no       | 最长256个字符            |
| create_user           | integer      | no       |                     |
| product_type          | integer/enum | yes      | 1无规格、2多规格、3组合       |
| model                 | string       | no       | 最长256个字符            |
| description           | string       | no       |                     |
| intro                 | string       | no       |                     |
| product_remark        | string       | no       |                     |
| images                | array        | no       |                     |
| from_url              | string       | no       |                     |
| hs_code               | string       | no       |                     |
| place                 | string       | no       |                     |
| info_json             | array        | no       |                     |
| quantity              | string       | no       |                     |
| quantity_unit         | string       | no       |                     |
| price_currency        | string       | no       |                     |
| price_min             | number/float | no       |                     |
| price_max             | number/float | no       |                     |
| price_unit            | string       | no       |                     |
| package_gross_weight  | string       | no       |                     |
| package_unit          | string       | no       |                     |
| package_size_length   | number/float | no       | 单位cm                |
| package_size_weight   | number/float | no       | 单位cm                |
| package_size_height   | number/float | no       | 单位cm                |
| package_volume        | number/float | no       | 单位m³                |
| product_size_length   | number/float | no       | 单位cm                |
| product_size_weight   | number/float | no       | 单位cm                |
| product_size_height   | number/float | no       | 单位cm                |
| product_volume        | number/float | no       | 单位m³                |
| group_id              | integer      | no       |                     |
| disable_flag          | integer/enum | no       | 1-是，0-否             |
| fob_type              | integer/enum | no       | 1单一区间定价,2阶梯定价,3规格定价 |
| gradient_price        | array        | no       |                     |
| sku_items             | array        | no       |                     |
| sub_product_sku_items | array        | no       |                     |
| images_base64         | array        | no       |                     |
| sku_attributes        | array        | no       | 多规格产品则必填            |
| count_per_carton      | number       | no       |                     |
| count_per_package     | number       | no       |                     |
| product_net_weight    | number       | no       |                     |
| carton_volume         | number       | no       |                     |
| carton_net_weight     | number       | no       |                     |
| carton_gross_weight   | number       | no       |                     |
| package_type          | number       | no       |                     |
| cost                  | number       | no       |                     |
| cost_currency         | string       | no       |                     |
| cost_unit             | string       | no       |                     |
| unit                  | string       | no       | 可以通过产品枚举接口获取计量单位值   |
| is_parts              | integer      | no       | 1是，0否               |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/product/push-groups

- operationId: `post_v1_product_push_groups`
- summary: 产品分组新增/编辑
- source: `../../sources/pages/api-3478264.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name      | type    | required | description                                                 |
| --------- | ------- | -------- | ----------------------------------------------------------- |
| group_id  | integer | no       | 编辑时必填，产品分组ID，与上级产品id不允许相同，可以从查询产品分组接口[/v1/product/groups]获得 |
| parent_id | integer | no       |                                                             |
| name      | string  | yes      |                                                             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/product/push-sku-attribute

- operationId: `post_v1_product_push_sku_attribute`
- summary: 新增/编辑规格
- source: `../../sources/pages/api-3478267.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name      | type    | required | description  |
| --------- | ------- | -------- | ------------ |
| item_id   | integer | no       | 产品规格ID，编辑时必填 |
| item_name | integer | yes      |              |
| node      | array   | yes      | 规格值列表        |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/product/remove

- operationId: `get_v1_product_remove`
- summary: 产品删除接口
- source: `../../sources/pages/api-3501017.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| query  | product_id    | string | no       | 要删除的CRM产品ID                              |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/product/remove-groups

- operationId: `post_v1_product_remove_groups`
- summary: 产品分组删除
- source: `../../sources/pages/api-3485272.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### requestBody
- contentType: `multipart/form-data` schema: `object`

| name     | type    | required | description                              |
| -------- | ------- | -------- | ---------------------------------------- |
| group_id | integer | yes      | 产品分组ID，可以从查询产品分组接口[/v1/product/groups]获得 |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| 404        | application/json |             |
| x-200:请求成功 | application/json |             |

## POST /v1/product/remove-sku-attribute

- operationId: `post_v1_product_remove_sku_attribute`
- summary: 删除产品规格
- source: `../../sources/pages/api-3478265.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name      | type    | required | description                                 |
| --------- | ------- | -------- | ------------------------------------------- |
| item_id   | integer | yes      | 可以从产品规格列表获取[/v1/product/sku-attribute-list] |
| item_name | integer | yes      |                                             |
| node      | array   | yes      |                                             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/product/sku-attribute-list

- operationId: `get_v1_product_sku_attribute_list`
- summary: 查询产品规格列表
- source: `../../sources/pages/api-3478269.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
