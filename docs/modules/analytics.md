# 统计分析

- generated_at: `2026-05-09T04:02:32+00:00`
- openapi: `../../openapi/modules/analytics.openapi.yaml`
- endpoints: `1`

## POST /v1/report/info

- operationId: `post_v1_report_info`
- summary: 统计报告-统计详细
- source: `../../sources/pages/api-3478247.md`

### parameters

| in     | name          | type   | required | description |
| ------ | ------------- | ------ | -------- | ----------- |
| header | Authorization | string | yes      |             |

### requestBody
- contentType: `application/json` schema: `object`

| name       | type   | required | description                            |
| ---------- | ------ | -------- | -------------------------------------- |
| key        | string | yes      | 统计类型，目前仅支持[xs1](工作量统计)，必填              |
| start_date | string | yes      | 获取统计的开始时间段例如2023-05-16，支持到天，必填         |
| end_date   | string | yes      | 获取统计的结束时间段例如2023-05-18，支持到天，必填         |
| user_id    | array  | no       | 小满员工账号user_id列表，[1,2,3,4]，非必填，默认获取全部员工 |
| refresh    | string | yes      | 刷新数据缓存，默认不传，如需获取最新数据，需要传【refresh=1】    |

### responses

| status | contentTypes     | description |
| ------ | ---------------- | ----------- |
| 200    | application/json |             |
