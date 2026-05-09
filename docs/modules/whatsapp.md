# WhatsApp

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/whatsapp.openapi.yaml`
- endpoints: `1`

## POST /v1/whatsapp/edw/getProfileByPlanId

- operationId: `post_v1_whatsapp_edw_getprofilebyplanid`
- summary: whatsapp代发对外接口
- source: `../../sources/pages/api-3498523.md`

### parameters

| in     | name          | type    | required | description |
| ------ | ------------- | ------- | -------- | ----------- |
| query  | plan_id       | integer | no       |             |
| header | Authorization | string  | no       |             |

### responses

| status     | contentTypes     | description |
| ---------- | ---------------- | ----------- |
| 200        | application/json |             |
| x-200:请求成功 | application/json |             |
