# VoiceBench coverage

<!-- Generated from data/voicebench.json and data/models.json. -->

[← Model list](../README.md#models)

**Reviewed 2026-09-13: 43 Open leaderboard rows; 40 mapped to public releases/systems, 3 exact checkpoints unverified.**

[Live leaderboard](https://matthewcym.github.io/VoiceBench/) · [Pinned source snapshot](https://github.com/MatthewCYM/VoiceBench/blob/6992cf4fc51d0426c52c4805b5002e0aae49118a/docs/index.html)

“Open” is the benchmark’s label, not a license certification. Our cards distinguish open licenses, custom/research restrictions and missing license declarations. Cascaded ASR + LLM baselines are counted as systems.

| VoiceBench entry | Catalog / release status | Notes |
| --- | --- | --- |
| BR-Voice-Reasoner | [BR-Voice-Reasoner](../models/omni.md#br-voice-reasoner) · Open license |  [Evidence 1](https://huggingface.co/brgroup/BR-Voice-Reasoner) |
| LFG-3 | [LFG-3](../models/audio.md#lfg-3) · License unclear | Public code and weights found; licensing is incomplete, as shown on the model card.  |
| NVIDIA Nemotron 3 Nano Omni 30B A3B | [Nemotron 3 Nano Omni](../models/omni.md#nemotron-3-nano-omni) · Custom / restricted |   |
| Ultravox-GLM-4P7 | Exact checkpoint unverified | VoiceBench evaluates a hosted GLM-4.7 endpoint. No exact GLM-4.7 checkpoint was located in the publisher’s public releases; GLM-4.6 is listed separately. [Evidence 1](https://github.com/MatthewCYM/VoiceBench/blob/6992cf4fc51d0426c52c4805b5002e0aae49118a/src/models/ultravox_glm4p7.py) · [Evidence 2](https://huggingface.co/fixie-ai) |
| Qwen3-Omni-30B-A3B-Thinking | [Qwen3-Omni Thinking](../models/omni.md#qwen3-omni-thinking) · Open license |  [Evidence 1](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking) |
| Ultravox-GLM-4P7 (thinking) | Exact checkpoint unverified | VoiceBench evaluates a hosted GLM-4.7 endpoint. No exact GLM-4.7 checkpoint was located in the publisher’s public releases; GLM-4.6 is listed separately. [Evidence 1](https://github.com/MatthewCYM/VoiceBench/blob/6992cf4fc51d0426c52c4805b5002e0aae49118a/src/models/ultravox_glm4p7.py) · [Evidence 2](https://huggingface.co/fixie-ai) |
| Ultravox-GLM-4P6 | [Ultravox 0.7 GLM-4.6](../models/audio.md#ultravox-0-7-glm-4-6) · Open license |   |
| LFG-2 | [LFG-2](../models/audio.md#lfg-2) · License unclear | Public code and weights found; licensing is incomplete, as shown on the model card.  |
| Qwen3-Omni-30B-A3B-Instruct | [Qwen3-Omni Instruct](../models/omni.md#qwen3-omni) · Open license |  [Evidence 1](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct) |
| Ultravox-v0.6-LLaMA-3.3-70B | [Ultravox 0.6 Llama-3.3-70B](../models/audio.md#ultravox-0-6-70b) · Custom / restricted |   |
| LFG-1 | [LFG-1](../models/omni.md#lfg-1) · Open license |   |
| Parakeet-TDT-0.6b-V2 + Qwen3-8B | [Parakeet-TDT-v2 + Qwen3-8B](../models/pipelines.md#parakeet-qwen3) · Open license | Both component checkpoints are public; the exact benchmark wrapper was not located.  |
| Whisper-v3-large + LLaMA-3.1-8B | [Whisper-v3-large + Llama-3.1-8B](../models/pipelines.md#whisper-v3-llama31) · Custom / restricted |   |
| Kimi-Audio | [Kimi-Audio](../models/speech.md#kimi-audio) · Open license |   |
| Whisper-v3-turbo + LLaMA-3.1-8B | [Whisper-v3-turbo + Llama-3.1-8B](../models/pipelines.md#whisper-turbo-llama31) · Custom / restricted |   |
| Ultravox-v0.5-LLaMA-3.1-8B | [Ultravox 0.5 Llama-3.1-8B](../models/audio.md#ultravox-0-5-8b) · Custom / restricted |   |
| Ultravox-v0.4.1-LLaMA-3.1-8B | [Ultravox 0.4.1 Llama-3.1-8B](../models/audio.md#ultravox-0-4-1) · Custom / restricted |   |
| Baichuan-Omni-1.5 | [Baichuan-Omni 1.5](../models/omni.md#baichuan-omni-1-5) · Custom / restricted |   |
| MiniCPM-o | [MiniCPM-o 2.6](../models/omni.md#minicpm-o-2-6) · Open license |   |
| Whisper-v3-turbo + LLaMA-3.2-3B | [Whisper-v3-turbo + Llama-3.2-3B](../models/pipelines.md#whisper-turbo-llama32) · Custom / restricted |   |
| Baichuan-Audio | [Baichuan-Audio](../models/speech.md#baichuan-audio) · Open license |   |
| MERaLiON | [MERaLiON-AudioLLM](../models/audio.md#meralion-audiollm) · Custom / restricted |   |
| VITA-1.5 | [VITA 1.5](../models/omni.md#vita-1-5) · Custom / restricted |   |
| Phi-4-multimodal | [Phi-4-multimodal](../models/omni.md#phi-4-multimodal) · Open license |   |
| Ola | [Ola](../models/omni.md#ola) · Open license |   |
| Lyra-Base | [Lyra-Base](../models/omni.md#lyra) · Custom / restricted |   |
| Nemotron 3 VoiceChat (V1) | Exact checkpoint unverified | The submission describes an early-access VoiceChat V1 release. Its exact checkpoint was not verified; the later public NemotronLabs VoiceChat 11B is a different release. [Evidence 1](https://github.com/MatthewCYM/VoiceBench/issues/29) · [Evidence 2](https://developer.nvidia.com/nemotron-voicechat-early-access) · [Evidence 3](https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B) |
| Ultravox-v0.5-LLaMA-3.2-1B | [Ultravox 0.5 Llama-3.2-1B](../models/audio.md#ultravox-0-5-1b) · Custom / restricted |   |
| DiVA | [DiVA](../models/audio.md#diva) · Custom / restricted |   |
| GLM-4-Voice | [GLM-4-Voice](../models/speech.md#glm-4-voice) · Custom / restricted |   |
| Qwen2-Audio | [Qwen2-Audio](../models/audio.md#qwen2-audio) · Open license |   |
| Freeze-Omni | [Freeze-Omni](../models/speech.md#freeze-omni) · Custom / restricted |   |
| Step-Audio | [Step-Audio](../models/speech.md#step-audio) · Open license |   |
| Megrez-3B-Omni | [Megrez-Omni](../models/omni.md#megrez-omni) · Open license |   |
| Ichigo | [Ichigo](../models/audio.md#ichigo) · License unclear |   |
| Lyra-Mini | [Lyra-Mini](../models/omni.md#lyra-mini) · Custom / restricted |   |
| Mair-hub-0.5B-Omni | [Mair-hub-0.5B-Omni](../models/speech.md#mair-hub-omni) · License unclear | Public code and weights found; licensing is incomplete, as shown on the model card.  |
| LLaMA-Omni | [LLaMA-Omni](../models/speech.md#llama-omni) · Custom / restricted |   |
| VITA-1.0 | [VITA 1.0](../models/omni.md#vita) · Custom / restricted |   |
| SLAM-Omni | [SLAM-Omni](../models/speech.md#slam-omni) · Open license |   |
| Mini-Omni2 | [Mini-Omni2](../models/omni.md#mini-omni2) · Open license |   |
| Mini-Omni | [Mini-Omni](../models/speech.md#mini-omni) · Open license |   |
| Moshi | [Moshi](../models/speech.md#moshi) · Open license |   |

Closed rows excluded: Whisper-v3-large + GPT-4o; GPT-4o-Audio; GPT-4o-mini-Audio.

Benchmark configurations and interaction labels can differ from the capabilities of the released checkpoint. The catalog records the selected checkpoint, rather than copying the benchmark’s architecture label.
