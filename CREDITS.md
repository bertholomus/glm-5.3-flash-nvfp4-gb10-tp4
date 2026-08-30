# Credits and provenance

BertholomusAI's contribution is independent deployment validation, operational hardening, sanitized evidence, and public test tooling. BertholomusAI did not create GLM-5.3, the NVFP4 checkpoint, or DFlash2.

## Direct deployed dependencies

- **Z.AI** — [`zai-org/GLM-5.3-Flash`](https://huggingface.co/zai-org/GLM-5.3-Flash), the upstream base model.
- **Red Hat AI / Neural Magic** — [`RedHatAI/GLM-5.3-Flash-NVFP4`](https://huggingface.co/RedHatAI/GLM-5.3-Flash-NVFP4), produced with [LLM Compressor](https://github.com/vllm-project/llm-compressor).
- **IncoAI** — [`incoai/GLM-5.3-Flash-DFlash2`](https://huggingface.co/incoai/GLM-5.3-Flash-DFlash2), the draft checkpoint used for speculative decoding.
- **vLLM contributors** — serving engine and OpenAI-compatible API.
- **NVIDIA** — GB10 hardware and CUDA platform.

## BertholomusAI original work

- checkpoint-integrity receipt and pinned manifest;
- one-variable scheduler/KV qualification ladder;
- bounded exact/tool/JSON/code/image/context/Unicode/concurrency gates;
- coordinated restart, watchdog, pressure, and queue-settlement qualification;
- sanitized evidence schema and public probe script.

All upstream names and marks belong to their respective owners. No endorsement is implied.
