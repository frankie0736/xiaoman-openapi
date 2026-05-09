# 授权登录

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/auth.openapi.yaml`
- endpoints: `2`

## POST /v1/oauth2/access_token

- operationId: `post_v1_oauth2_access_token`
- summary: 鉴权接口
- source: `../../sources/pages/api-3473041.md`

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

| name          | type   | required | description                                                                                                                                                      |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type    | string | yes      | 授权模式 password 或 client_credentials                                                                                                                               |
| client_id     | string | yes      | 登录主账号：OKKI CRM → 进入企业管理 → 外部对接 → API对接获取client_id                                                                                                                |
| client_secret | string | yes      | 登录主账号：OKKI CRM → 进入企业管理 → 外部对接 → API对接获取client_secret                                                                                                            |
| username      | string | no       | 小满的登录邮箱，当client_credentials时不用传                                                                                                                                  |
| password      | string | no       | 密码需要使用SHA 256加密，当client_credentials是不用传                                                                                                                          |
| scope         | string | yes      | 授权访问的业务API列表，中间加半角空格分割，目前开放 product(产品) company(公司客户) lead(线索) opportunity(商机) invoices(订单、报价单、回款单) user(用户列表) costInvoice(费用单) paymentInvoice(付款单) purchaseOrd… |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |

## POST /v1/oauth2/refresh_token

- operationId: `post_v1_oauth2_refresh_token`
- summary: 刷新令牌接口
- source: `../../sources/pages/api-3483803.md`

### requestBody
- contentType: `application/x-www-form-urlencoded` schema: `object`

| name          | type   | required | description                  |
| ------------- | ------ | -------- | ---------------------------- |
| grant_type    | string | yes      | 授权模式，默认值: refresh_token      |
| refresh_token | string | yes      | 刷新令牌，从鉴权接口中获取到的refresh_token |
| client_id     | string | yes      | 客户端身份标识（平台发放）                |
| client_secret | string | yes      | 客户端密钥（平台发放）                  |

### responses

| status       | contentTypes     | description |
| ------------ | ---------------- | ----------- |
| 200          | application/json |             |
| 400          | application/json |             |
| x-400:刷新令牌无效 | application/json |             |
