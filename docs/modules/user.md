# 用户

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/user.openapi.yaml`
- endpoints: `4`

## GET /v1/user/departmentInfo

- operationId: `get_v1_user_departmentinfo`
- summary: 用户部门详情
- source: `../../sources/pages/api-3478461.md`

### parameters

| in     | name            | type    | required | description                              |
| ------ | --------------- | ------- | -------- | ---------------------------------------- |
| query  | department_id   | integer | no       | 需要查询部门id                                 |
| query  | department_name | string  | no       | 需要查询部门名称                                 |
| header | Authorization   | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/user/departmentList

- operationId: `get_v1_user_departmentlist`
- summary: 用户部门列表
- source: `../../sources/pages/api-3478460.md`

### parameters

| in     | name          | type   | required | description                              |
| ------ | ------------- | ------ | -------- | ---------------------------------------- |
| header | Authorization | string | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |

## GET /v1/user/info

- operationId: `get_v1_user_info`
- summary: 用户详情
- source: `../../sources/pages/api-3478291.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | user_id       | integer | no       | 需要查询用户ID                                 |
| query  | email         | string  | no       | 需要查询用户邮箱                                 |
| query  | nickname      | string  | no       | 用户昵称                                     |
| query  | full_name     | string  | no       | 用户姓名                                     |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## GET /v1/user/list

- operationId: `get_v1_user_list`
- summary: 用户列表
- source: `../../sources/pages/api-3478290.md`

### parameters

| in     | name          | type    | required | description                              |
| ------ | ------------- | ------- | -------- | ---------------------------------------- |
| query  | enable_flag   | integer | no       | 默认1，0冻结，1正常，2已删除                         |
| header | Authorization | string  | yes      | 从/v1/oauth2/access_token获取到的access_token |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
