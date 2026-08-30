---
license: mit
library_name: vllm
pipeline_tag: text-generation
base_model:
- zai-org/GLM-5.3-Flash
- RedHatAI/GLM-5.3-Flash-NVFP4
tags:
- glm-5.3
- vllm
- dgx-spark
- gb10
- distributed-inference
- tensor-parallel
- speculative-decoding
- dflash2
- long-context
- nvfp4
- multimodal
---

# GLM-5.3-Flash NVFP4 on 4× NVIDIA GB10 (TP4)

> **Independent BertholomusAI deployment-validation and evidence package. No model weights are hosted here.**

This repository mirrors the sanitized evidence, integrity receipt, and public probe tooling from the canonical GitHub release:

- GitHub: https://github.com/bertholomus/glm-5.3-flash-nvfp4-gb10-tp4
- Upstream target: https://huggingface.co/RedHatAI/GLM-5.3-Flash-NVFP4
- Upstream base: https://huggingface.co/zai-org/GLM-5.3-Flash
- Optional draft used in the validation: https://huggingface.co/incoai/GLM-5.3-Flash-DFlash2

## Validated formula

- 4× NVIDIA GB10, TP4
- Red Hat NVFP4 revision `36c184c6cda000a481711306df5adde42f63321a`
- FP8 KV, 24 GiB/rank
- 8,192 maximum batched tokens
- DFlash2 depth 7
- 1,048,576 configured context
- 260,066-token strongest exact retrieval receipt
- two concurrent 240,073-token exact boundary retrievals
- native tools, tool continuation, strict JSON, executable Python, image input, Korean Unicode integrity, six-request bounded concurrency, restart and queue-settlement gates

## Honest limits

- “Configured 1M” is not a claim that exact 1M retrieval was proven.
- DFlash2 is separately licensed; its repository reports `CC BY-NC-ND 4.0`. No weights are mirrored or modified here.
- The Red Hat checkpoint page does not currently expose explicit derivative-license metadata; this repository links rather than mirrors it.
- Earlier Unicode comparison runs used non-identical recorded output caps, so no controlled corruption headline is made.
- One low-budget arithmetic answer varied across earlier rungs. No quality gain is attributed to KV size.
- No BF16-parity, “fastest,” “first,” or universal speedup claim is made.

See `evidence/qualification.json`, `evidence/kv-ladder.json`, and `evidence/checkpoint-manifest.json` for machine-readable receipts. Licensing and attribution are documented in `CREDITS.md` and `NOTICE`.
