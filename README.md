# GLM-5.3-Flash NVFP4 on 4× NVIDIA GB10 (TP4)

> **Archived.** This GLM-5.3-Flash NVFP4 validation recipe is no longer maintained. For GLM-5.3 on four DGX Sparks, see [bertholomus/glm-5.3-exlr8-4x-spark](https://github.com/bertholomus/glm-5.3-exlr8-4x-spark). This repository is read-only.

> **Independent BertholomusAI deployment-validation and evidence package.** This repository contains no model weights and is not affiliated with Z.AI, Red Hat, IncoAI, NVIDIA, or the vLLM project.

This package documents a qualified four-node tensor-parallel deployment of [`RedHatAI/GLM-5.3-Flash-NVFP4`](https://huggingface.co/RedHatAI/GLM-5.3-Flash-NVFP4), derived from [`zai-org/GLM-5.3-Flash`](https://huggingface.co/zai-org/GLM-5.3-Flash), with FP8 KV cache and the separately licensed [`incoai/GLM-5.3-Flash-DFlash2`](https://huggingface.co/incoai/GLM-5.3-Flash-DFlash2) draft.

## What we validated

| Surface | Observed result |
|---|---|
| Hardware topology | 4× NVIDIA GB10, TP4 |
| Target checkpoint | Red Hat NVFP4, revision `36c184c6cda000a481711306df5adde42f63321a` |
| Checkpoint receipt | 21 files, 197,881,157,135 bytes |
| Advertised context | 1,048,576 tokens |
| Strongest exact retrieval | 260,066 prompt tokens |
| Concurrent retrieval | 2 × 240,073-token prompts; both boundary pairs exact |
| Tool behavior | Native tool call and tool-result continuation passed |
| Other gates | Exact output, strict JSON, executable Python, image input, Korean Unicode integrity |
| Speculation | DFlash2, depth 7; activity verified through nonzero draft/accepted-token counters |
| Scheduler | 8,192 max batched tokens |
| Qualified KV rung | 24 GiB/rank; 3,895,606 reported KV tokens; 3.72× calculated maximum-length concurrency |
| Useful short concurrency | 6 simultaneous bounded generations passed |

Machine-readable receipts are in [`evidence/`](evidence/). The public evidence intentionally excludes endpoint addresses, response IDs, credentials, internal hostnames, service names, and consumer identities.

## Runtime formula

- vLLM-compatible GLM-5.3 runtime on SM121/GB10
- tensor parallelism: 4
- `max_model_len`: 1,048,576
- `max_num_seqs`: 6
- `max_num_batched_tokens`: 8,192
- block size: 2,304
- explicit KV allocation: 25,769,803,776 bytes/rank
- KV dtype: `fp8_e4m3`
- eager execution
- target MoE backend: `marlin`
- DFlash2 depth: 7
- tool parser: `glm47`
- reasoning parser: `glm45`

See [`config/runtime-formula.json`](config/runtime-formula.json). The exact local serving image was identified by image ID, not a public registry digest, so this is presently an **evidence-backed operational formula**, not a byte-for-byte public image reproduction.

## Proof gates

The harness validates bounded observable behavior rather than claiming general intelligence or BF16 parity:

1. exact visible response;
2. native function call;
3. tool-result continuation;
4. strict JSON;
5. three bounded arithmetic/reasoning cases;
6. executable Python;
7. deterministic image-color input;
8. exact two-boundary long-context retrieval;
9. Korean U+FFFD replacement-character probe;
10. concurrent long-context retrieval;
11. six-request bounded concurrency;
12. queue settlement, rank health, pressure, and coordinated restart.

## Important limitations

- **Configured 1M context is not the same as proven 1M retrieval.** The strongest exact retrieval receipt here is 260,066 prompt tokens.
- DFlash2 acceptance and throughput are workload-dependent.
- Earlier 8K-batching and 20 GiB KV runs each produced one low-budget arithmetic miss (`6` instead of `7`); the 24 GiB run returned `7`. This is model variance, not evidence that KV size improves reasoning.
- The historical incumbent and candidate Korean probes did not use identical recorded output caps. A same-parameter public A/B is required before publishing a comparative corruption headline.
- No BF16-parity, universal speedup, “fastest,” or “first” claim is made.
- The deployment used a custom serving image whose public build closure is not yet included.

## Checkpoint integrity

[`evidence/checkpoint-manifest.json`](evidence/checkpoint-manifest.json) records the pinned repository revision, file sizes, available LFS SHA-256 values, and Git blob IDs. It is a verification receipt, not a redistribution of weights.

## Licensing

- Original BertholomusAI scripts and documentation in this repository: MIT; see [`LICENSE`](LICENSE).
- Z.AI base model: MIT; preserve its upstream notice.
- The Red Hat repository identifies itself as an LLM Compressor NVFP4 quantization but currently exposes no explicit repository license metadata. This package links to it and does **not** mirror its weights.
- The DFlash2 repository reports `CC BY-NC-ND 4.0`. This package does not mirror or modify it. Review its terms before use, especially commercial use.

See [`CREDITS.md`](CREDITS.md) and [`NOTICE`](NOTICE).

## Reproduction

Start with the pinned upstream artifacts, adapt [`config/runtime-formula.json`](config/runtime-formula.json) to your network/storage layout, then run the public harness against your OpenAI-compatible endpoint:

```bash
python3 scripts/probe_openai.py \
  --base-url http://127.0.0.1:8000/v1 \
  --model glm-5.3-flash \
  --output evidence/local-smoke.json
```

Do not expose an unauthenticated endpoint beyond a trusted network.

## Citation

See [`CITATION.cff`](CITATION.cff).
