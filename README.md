# xiaoman-openapi

Unofficial AI-readable OpenAPI and Markdown bundle for Xiaoman Open API.

## Invariant

The public Xiaoman `.md` pages are the input source. Generated OpenAPI files and agent Markdown are derived artifacts. Do not edit generated files by hand; update the sync script and regenerate.

## Files

- `openapi/xiaoman.openapi.yaml`: full merged OpenAPI 3.0.1 document.
- `openapi/modules/*.openapi.yaml`: module-level OpenAPI documents.
- `docs/modules/*.md`: compact agent-facing Markdown generated from OpenAPI operations.
- `docs/api-index.md`: endpoint table for quick retrieval.
- `docs/guides-index.md`: local index of non-endpoint Xiaoman guide pages.
- `docs/source-index.md`: local source snapshot index.
- `docs/external/yuque/*.md`: AI-facing summaries for linked Yuque guide snapshots.
- `docs/agent/endpoints.jsonl`: one endpoint per line for embedding/indexing pipelines.
- `sources/pages/*.md`: fetched public Xiaoman Markdown pages.
- `sources/external/`: mirrored external guide snapshots linked from Xiaoman pages.
- `assets/images/`: mirrored Markdown images used by the guide pages.
- `reports/sync-report.json`: extraction warnings and conflict report.
- `reports/external-links.json`: classified external URLs found in generated text files.

## How AI Agents Should Use This

Start from the smallest stable context, then load the exact contract only when needed.

1. Read `llms.txt` as the repository entry point.
2. Locate the endpoint in `docs/api-index.md` or `docs/agent/endpoints.jsonl`.
3. Read the matching `docs/modules/<module>.md` for compact human-readable context.
4. Use `openapi/modules/<module>.openapi.yaml` as the request/response contract.
5. Use `sources/pages/*.md` only when you need to inspect the mirrored Xiaoman page content.
6. Use `docs/guides-index.md` and `docs/external/yuque.md` for onboarding and linked guide context.

Do not load `openapi/xiaoman.openapi.yaml` into an LLM context by default. The full file is for OpenAPI tools, code generators, validators, and offline indexing. Agent workflows should prefer module specs.

### Remote Agent Prompt

```text
You are integrating with Xiaoman Open API.
First read:
https://raw.githubusercontent.com/frankie0736/xiaoman-openapi/main/llms.txt

Find endpoints via docs/api-index.md or docs/agent/endpoints.jsonl.
For implementation, use the matching openapi/modules/*.openapi.yaml file as the source of truth.
Do not infer request fields from the web UI. If Markdown and OpenAPI conflict, trust OpenAPI.
```

### Use Inside Another Repository

```bash
git submodule add https://github.com/frankie0736/xiaoman-openapi docs/vendor/xiaoman-openapi
```

Then point your coding agent at:

```text
docs/vendor/xiaoman-openapi/llms.txt
docs/vendor/xiaoman-openapi/docs/api-index.md
docs/vendor/xiaoman-openapi/openapi/modules/*.openapi.yaml
```

### RAG / Tooling Input

Use `docs/agent/endpoints.jsonl` for retrieval. Each line is one endpoint with module, method, path, parameters, request body summary, responses, and local source path. After retrieval, load the module OpenAPI file before generating code.

## Offline Coverage

The API guide is offline-complete for the official public pages listed in Xiaoman's `llms.txt` at sync time. Those pages are copied to `sources/pages/`, generated guides point to local files, and each generated endpoint includes `source` / `localSource` / `x-local-source-path` pointing back to the local snapshot.

Markdown images used by guide pages are mirrored under `assets/images/`. Yuque guide links referenced by Xiaoman pages are mirrored under `sources/external/yuque/` with AI-facing summaries in `docs/external/yuque/`.

Remaining external URLs are classified in `reports/external-links.json`. They should be runtime API servers, example payload values, repository usage links, attribution metadata, or assets embedded inside archived external HTML snapshots. They are not required to read the API guide offline.

## Modules

- [统计分析](docs/modules/analytics.md): `analytics`
- [授权登录](docs/modules/auth.md): `auth`
- [资金](docs/modules/capital-account.md): `capital-account`
- [客户](docs/modules/company.md): `company`
- [费用单](docs/modules/cost-invoice.md): `cost-invoice`
- [devops相关](docs/modules/devops.md): `devops`
- [示例接口（勿用）](docs/modules/example-do-not-use.md): `example-do-not-use`
- [线索](docs/modules/lead.md): `lead`
- [商机](docs/modules/opportunity.md): `opportunity`
- [付款单](docs/modules/payment.md): `payment`
- [产品](docs/modules/product.md): `product`
- [采购入库单](docs/modules/purchase-inbound.md): `purchase-inbound`
- [采购订单](docs/modules/purchase-order.md): `purchase-order`
- [采购退货单](docs/modules/purchase-return.md): `purchase-return`
- [报价单](docs/modules/quotation.md): `quotation`
- [回款单](docs/modules/receipt.md): `receipt`
- [回款登记](docs/modules/receipt-registration.md): `receipt-registration`
- [销售订单](docs/modules/sales-order.md): `sales-order`
- [销售出库单](docs/modules/sales-outbound.md): `sales-outbound`
- [供应商](docs/modules/supplier.md): `supplier`
- [用户](docs/modules/user.md): `user`
- [库存](docs/modules/warehouse.md): `warehouse`
- [消息推送](docs/modules/webhook.md): `webhook`
- [WhatsApp](docs/modules/whatsapp.md): `whatsapp`

## Regenerate

```bash
python3 -m pip install -r requirements.txt
python3 tools/sync_xiaoman_docs.py
python3 tools/validate_openapi.py
python3 tools/check_offline_docs.py
python3 tools/check_no_secrets.py
```

## Source

- catalog: `https://open.xiaoman.cn/llms.txt`
- official site: `https://open.xiaoman.cn`
- last generated: `2026-05-09T04:02:32+00:00`
- fetched pages: `154`
- extracted endpoints: `127`

## Notice

This repository is not affiliated with Xiaoman. API descriptions are generated from publicly available Xiaoman documentation. Xiaoman owns its product names and official documentation content. See `NOTICE.md`.

## License

Repository tooling is MIT licensed. Generated documentation is derived from Xiaoman public documentation and may be subject to Xiaoman's original terms.
