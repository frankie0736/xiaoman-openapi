# 资金

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/capital-account.openapi.yaml`
- endpoints: `1`

## GET /v1/capitalAccount/list

- operationId: `get_v1_capitalaccount_list`
- summary: 资金账户列表
- source: `../../sources/pages/api-3478248.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | count         | string  | no       | 每页数量，默认值 10                              |
| query  | start_index   | integer | no       | 页码                                       |
| query  | status        | integer | no       | 资金账户状态：1-启用，2-停用                         |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
