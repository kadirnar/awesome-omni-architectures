# Scope, research method and reading guide

[← Model index](../README.md#models)

This catalog is a public-source research snapshot dated **2026-09-12**. Its goal is broad coverage of omni and spoken language model research, including historical work and current documented releases. It is not an exhaustive census of private models, all fine-tunes or all checkpoint files.

## Scope

The main catalog covers six complementary areas:

1. **Omni and audiovisual language models:** language-centered models that connect audio/speech and vision, as well as explicitly labeled multimodal systems. Some understand several modalities but generate only text. Others use separate output generators.
2. **Spoken dialogue:** models with a documented speech response path, including research configurations, open releases and proprietary API models.
3. **Foundations:** textless speech LMs, joint speech-text pretraining, continuous audio LMs and multilingual speech/text generation. Older encoder-decoder and masked-pretraining models are included as foundations even when they are not modern chat LLMs.
4. **Audio understanding:** language models answering in text about speech, environmental sounds or music.
5. **LLM-based ASR and translation:** speech recognition/translation with a documented language-model connection. This is a subset of speech recognition research.
6. **Speech generation:** autoregressive codec LMs, masked generative token models, diffusion language models and continuous-latent autoregressive approaches to speech synthesis.

The [related section](../models/related.md) retains selected boundary cases: visual/3D omni models, multimodal diffusion generators and modular speech systems. These have a separate count. Their inclusion does not classify them as speech language models.

A model with “Omni” in its name is not automatically audiovisual. Conversely, a model can meet this catalog's omni scope without using that name. A speech or music subtype does not count as an extra independent audio modality.

## Research procedure

Discovery combined the survey collections below with searches for model names, successors, full-duplex interaction, audio reasoning, speech-text pretraining and LM-based TTS. Candidate entries were checked against author papers, official repositories, model cards and vendor documentation. Vendor indexes were inspected for newer versions rather than assuming a remembered model list was current.

Each included record links at least one primary source. A source title is retained in the JSON so that incorrect name-to-paper matches can be spotted. Entries summarize the publicly described architecture and capabilities; they do not copy benchmark tables or rank incomparable evaluations.

Review depth is explicit in `sources[].review_level`:

| Review level | Evidence inspected | Practical limit |
| --- | --- | --- |
| `abstract` | Author abstract and paper metadata, with further primary materials where needed. | Not a full-paper reproduction or a claim that every implementation detail was audited. |
| `readme` | Official repository README. | README capabilities may span checkpoints, development branches or planned releases; notes limit the entry accordingly. |
| `model-card` | Publisher's model card. | Applies to the specified model or documented family. |
| `documentation` | Official model/API documentation. | A public interface does not expose every internal architectural component. |
| `announcement` | Official dated release/research announcement. | Reported capabilities are not independently measured here. |
| `project` | Author or vendor project page. | Missing technical details remain unspecified. |

High-level architecture phrases are editorial summaries of those sources, not a claim that the models were independently implemented. No model weights were downloaded and no inference, latency or quality benchmarks were run for this catalog. The repository's automated check validates catalog integrity and local links; it does not certify remote endpoint availability or scientific claims.

## Counting and versions

The unit of counting is an **entry**, not a unique architecture, parameter size or downloadable checkpoint. Major published generations and materially different API interfaces can have separate entries. Base/Instruct, size variants, speaker variants and minor checkpoint versions usually share a row. Explicitly named fine-tuned research models can have their own rows and are described as derivatives when established.

Each entry has one primary category. A speech-generating omni model is not repeated in the dialogue section. A research system can include other listed models without becoming a new base architecture. Category totals therefore describe this inventory, not the number of independent technical inventions.

The `variants` array is a list of verified names useful for discovery, not an exhaustive list of every quantization or snapshot. A family's input/output columns can span variants; the notes and exact source identify restrictions. For example, a Captioner checkpoint does not inherit the speech output of an Instruct checkpoint merely because both belong to Qwen3-Omni.

Historical and preview entries are retained. “Included” does not mean available, downloadable, open weight, open source or commercially licensed. Architecture disclosure, code availability and weights licensing are different questions; no uniform openness classification is inferred from a GitHub link.

## Modalities and interaction

| Symbol | Meaning | Reading rule |
| --- | --- | --- |
| T | Text | Includes transcripts and text-serialized answers. Text prompting does not always mean unrestricted text chat. |
| I | Images | Still-image input/output; do not infer a native video stream from repeated image uploads. |
| V | Video | A documented video path, often implemented through frame sampling. |
| A | General audio | Broad audio scope or a general audio API; not a promise to understand/generate every kind of sound. |
| S | Speech | Spoken language. In TTS, input S often means a voice reference or continuation prompt. |
| M | Music | Music-specific modeling. |
| X | Other | Grounding, masks, coordinates, motion, sensors or actions; see the entry's notes. |

The tables summarize documented paths, not a Cartesian product of every possible input-output combination. Grounding or actions can use external components in entries marked `system`. Spoken input with a text response is not speech-to-speech generation. Text-to-speech of a supplied dialogue is not an assistant that invents the reply.

`streaming` means incremental processing or output is documented. It does not establish full duplex, a particular latency, interruption handling or a released streaming server. `full-duplex` is reserved for an explicit source description of concurrent listening and speaking. These are reported capabilities, not independently verified real-time guarantees. `not-specified` preserves uncertainty.

## Architectural patterns

These patterns overlap. A model can combine a pretrained text backbone, modality encoders, expert routing and a separate acoustic decoder. Follow the linked entries for their primary sources.

| Pattern | What is modeled | Examples |
| --- | --- | --- |
| Speech units and textless language modeling | Predict discrete speech units, then reconstruct a waveform. | [GSLM](../models/speech-foundations.md#gslm), [TWIST](../models/speech-foundations.md#twist). |
| Shared multimodal token sequences | Express several modalities as a sequence for language-model prediction. | [AnyGPT](../models/omni.md#anygpt), [MIO](../models/omni.md#mio), [VideoPoet](../models/omni.md#videopoet). |
| Encoder–adapter–LLM | Map audio or visual features into a language model; output can remain textual. | [SALMONN](../models/audio-understanding.md#salmonn), [Qwen2-Audio](../models/audio-understanding.md#qwen2-audio), [Ultravox](../models/audio-understanding.md#ultravox). |
| Thinker–Talker | Separate multimodal reasoning/text generation from a speech-generation path. | [Qwen2.5-Omni](../models/omni.md#qwen2-5-omni), [Qwen3-Omni](../models/omni.md#qwen3-omni). |
| Multistream and delayed decoding | Align incoming audio, outgoing audio and text along time. | [Moshi](../models/speech-dialogue.md#moshi), [Hibiki](../models/speech-foundations.md#hibiki), [Kyutai STT](../models/llm-asr.md#kyutai-stt-dsm). |
| MoE and modality routing | Route representations through specialized experts. | [Uni-MoE](../models/omni.md#uni-moe), [Ming-Omni](../models/omni.md#ming-omni). |
| Codec language modeling for TTS | Predict acoustic or semantic tokens conditioned on text and a voice reference. | [VALL-E](../models/speech-generation.md#vall-e), [CosyVoice](../models/speech-generation.md#cosyvoice), [Llasa](../models/speech-generation.md#llasa). |
| Masked or diffusion token LMs | Fill missing speech tokens through non-autoregressive generation. | [MaskGCT](../models/speech-generation.md#maskgct), [OmniVoice](../models/speech-generation.md#omnivoice). |
| Continuous autoregressive generation | Predict continuous acoustic latents with a flow/diffusion/consistency head. | [CALM](../models/speech-foundations.md#calm), [TADA](../models/speech-foundations.md#tada), [VibeVoice](../models/speech-generation.md#vibevoice), [VoxCPM](../models/speech-generation.md#voxcpm). |
| External generators or cascaded systems | A language model coordinates separately implemented generation components. | [NExT-GPT](../models/omni.md#next-gpt), [FireRedChat](../models/related.md#fireredchat). |

## Figures

Every model entry has a local visual recorded in [data/figures.json](../data/figures.json). Primary-source architecture, training or method figures are preferred; [credits](../assets/architectures/CREDITS.md) retain the source, image/PDF origin and figure locator. PDF crops and rasterized figures preserve technical content, and source figures retain their original rights.

When no suitable source figure was obtained, a labeled editorial SVG shows the catalog's documented inputs and outputs. These interface summaries do not infer unpublished internals or imply that every input/output combination is supported. Family figures can be shared across entries when the cited source covers both; the model notes still qualify variants and external components.

## Dates

`as_of` is the catalog snapshot date. `sources[].reviewed_on` is the review date. Neither is a model release date.

`source_date` is the linked paper's submission/publication date or an explicitly dated official announcement; `source_date_kind` identifies which. It is null when a date was not established. Repository activity dates, training cutoffs, API snapshot suffixes and dates embedded in arbitrary URLs are not substituted for release dates.

The [timeline](timeline.md) is consequently a **paper and announcement timeline**. The first version of a paper can precede newer variants described in an updated manuscript. Model weights and APIs may be released before or after the paper. When several model entries share a paper, the repeated source date does not establish simultaneous model release.

## Name and source corrections

| Potential confusion | Treatment |
| --- | --- |
| BuboGPT linked to the NExT-GPT paper in a discovery list | BuboGPT uses its own [2307.08581 paper](https://arxiv.org/abs/2307.08581); NExT-GPT uses [2309.05519](https://arxiv.org/abs/2309.05519). |
| OpenOmni and Omni-Emotion sharing a paper link | [2501.04561](https://arxiv.org/abs/2501.04561) is OpenOmni. The thin [Omni-Emotion repository](https://github.com/HumanMLLM/Omni-Emotion) did not resolve the conflicting paper/capability evidence, so Omni-Emotion is pending rather than assigned OpenOmni's claims. |
| Multiple Omni-R1 papers | [Audio reasoning](https://arxiv.org/abs/2505.09439) and [two-system collaboration](https://arxiv.org/abs/2505.20256) have disambiguated entries. [R1-Omni](https://arxiv.org/abs/2503.05379) is another model. |
| Spectron name collision | The catalog uses the [speech-QA model](https://arxiv.org/abs/2305.15255), not the unrelated speaker-extraction work. |
| OmniGAIA, EgoLife, SAVEn-Vid and OmniAVS | The relevant trained models are OmniAtlas, EgoGPT, SAVEnVideo and OISA. Datasets/benchmarks are not counted as additional models. |
| Parrot and NTPP | Related workshop and later paper names are grouped, avoiding a duplicate model-family count. |
| Qwen2-Audio and Ultravox voice-chat descriptions | Their documented language-model output is text; a voice application can add TTS. |
| CSM, Dia, ChatTTS, MOSS-TTSD and VibeVoice | Conversational speech rendering is distinguished from autonomous spoken dialogue. |
| GPT-4o research capability versus API capability | A reported-model row is separate from audio, realtime, transcription and TTS interfaces. |
| SALMONN, SALMONN-2, video-SALMONN and SALMONN-omni | Hearing, video understanding and full-duplex speech are kept as distinct releases. |

## Exclusions and remaining gaps

- Tokenizers, codecs, vocoders and encoders such as EnCodec, Mimi, HuBERT, WavLM and wav2vec 2.0 are components, not standalone generative SpeechLM entries.
- Conventional ASR families such as Whisper, SenseVoice and standalone CTC/AED models are not enumerated as LLM-based ASR. A release that has both AED and LLM branches contributes its LLM branch to the main catalog.
- Pure acoustic diffusion/flow TTS such as Voicebox, E2 TTS and F5-TTS is not relabeled as language modeling. Continuous *autoregressive* language modeling, and discrete masked/diffusion **language models**, are included where the source establishes that formulation.
- Text/image-only VLMs, music-only generators and video generators are not exhaustively covered. Selected “omni” boundary cases are retained in the related section.
- Libraries and infrastructure such as VeOmni, vLLM-Omni and SGLang-Omni are not models. Benchmarks, datasets and training-only recipes without a named model are not automatically counted.
- A product's voice button or an API's speech feature does not prove a new native SpeechLM architecture. Product-only claims, inaccessible announcements and ambiguous same-name entries need stronger primary evidence before entering the main catalog.
- Private models, unannounced research, every regional deployment, all fine-tunes and all checkpoint revisions remain outside a verifiable completeness claim. New supported entries are welcome through the [contribution process](../CONTRIBUTING.md).

## Discovery references

Surveys and community lists were used to discover candidates and terminology. Model-level claims use primary sources linked in the catalog.

- [Recent Advances in Speech Language Models: A Survey](https://aclanthology.org/2025.acl-long.682/) and its [maintained collection](https://github.com/dreamtheater123/Awesome-SpeechLM-Survey).
- [On the Landscape of Spoken Language Models: A Comprehensive Survey](https://arxiv.org/abs/2504.08528).
- [From Specific-MLLMs to Omni-MLLMs: A Survey](https://arxiv.org/abs/2412.11694) and the [omni-model collection](https://github.com/threegold116/Awesome-Omni-MLLMs).
- [Full-duplex speech dialogue survey](https://arxiv.org/abs/2509.14515) and [DuplexSurvey](https://github.com/MM-Speech/DuplexSurvey).
- [Speaking While Listening survey](https://arxiv.org/abs/2606.19453).
- [Awesome large audio-language models](https://github.com/snkii/awesome-lalm) and [Speech-LLMs progress](https://github.com/xiaozhang521/Speech-LLMs-progress).
- Official [OpenAI model documentation](https://developers.openai.com/api/docs/models), [Gemini model documentation](https://ai.google.dev/gemini-api/docs/models), publisher model cards and project repositories for release-specific updates.
