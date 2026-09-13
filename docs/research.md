# Research trail

[← Model list](../README.md#models)

Reviewed **2026-09-13**. Discovery combines VoiceBench, speech-language-model surveys, cited papers and the authors' release repositories. Model descriptions summarize documented purposes; architecture notes come from the cited paper sections, model cards or implementation documentation.

## Discovery sources

| Primary source | How it was used |
| --- | --- |
| [VoiceBench paper](https://arxiv.org/abs/2410.17196), [leaderboard](https://matthewcym.github.io/VoiceBench/) and [repository](https://github.com/MatthewCYM/VoiceBench) | Audit every Open leaderboard row, then follow the repository's voice-assistant reading list |
| [Recent Advances in Speech Language Models: A Survey](https://arxiv.org/abs/2410.03751) and [author bibliography](https://github.com/dreamtheater123/Awesome-SpeechLM-Survey) | Find foundational audio language models and speech interaction families |
| [From Turn-Taking to Synchronous Dialogue](https://arxiv.org/abs/2509.14515) and [author bibliography](https://github.com/elpsykongloo/FD-SLMs) | Expand streaming and full-duplex coverage |
| [A Survey of Full-Duplex Spoken Dialogue Systems](https://arxiv.org/abs/2606.19453) and [author bibliography](https://github.com/MM-Speech/DuplexSurvey) | Follow newer dialogue architectures and release references |

A bibliography entry is a lead, not proof of a public model. Each catalog record links its actual implementation and checkpoint. Published weight files were inspected through their repository listings; weights were not downloaded or benchmarked. The [timeline](timeline.md) and [JSON sources](../data/models.json) retain per-model citations and review levels.

## Paper-driven additions

| Area | Examples and primary papers |
| --- | --- |
| Efficient local speech | [LFM2-Audio](https://arxiv.org/abs/2511.23404), [LFM2.5-Audio model card](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B), [Japanese adaptation](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP) |
| Spoken conversation | [Kimi-Audio](https://arxiv.org/abs/2504.18425), [MiMo-Audio](https://arxiv.org/abs/2512.23808), [Step-Audio 2](https://arxiv.org/abs/2507.16632), [OpenS2S](https://arxiv.org/abs/2507.05177) |
| Full-duplex dialogue | [Moshi](https://arxiv.org/abs/2410.00037), [Voila](https://arxiv.org/abs/2505.02707), [Lychee-FD](https://arxiv.org/abs/2607.06540), [DuplexCascade](https://arxiv.org/abs/2603.09180) |
| Audio understanding and reasoning | [DIFFA-2](https://arxiv.org/abs/2601.23161), [MOSS-Audio](https://arxiv.org/abs/2606.01802), [Audio Flamingo Next](https://arxiv.org/abs/2604.10905), [SALMONN-2](https://arxiv.org/abs/2607.17079) |
| Interaction and paralinguistic cues | [ParaBridge](https://arxiv.org/abs/2606.10581), [Audio-Interaction](https://arxiv.org/abs/2606.05121), [Sympatheia](https://arxiv.org/abs/2606.00851), [VoxMind](https://arxiv.org/abs/2604.15710) |
| Audiovisual models | [Nemotron 3 Nano Omni](https://arxiv.org/abs/2604.24954), [Audio-Visual Flamingo](https://arxiv.org/abs/2607.16107), [Uni-MoE 2.0 Omni](https://arxiv.org/abs/2511.12609) |
| Speech recognition language models | [Granite Speech](https://arxiv.org/abs/2505.08699), [Qwen3-ASR](https://arxiv.org/abs/2601.21337), [Voxtral](https://arxiv.org/abs/2507.13264), [VibeVoice-ASR](https://arxiv.org/abs/2601.18184) |

The tables are discovery examples; the complete included model list, short purpose text and image are in the [README](../README.md#models). Family publications can cover several later checkpoints; those releases are identified separately without assigning a guessed release date.

## Release gaps and exclusions

| Candidate | Review outcome |
| --- | --- |
| Ultravox GLM-4.7, including thinking mode | VoiceBench's wrapper calls a hosted endpoint; no exact public checkpoint was located. Public GLM-4.6 is a separate entry. [Coverage evidence](voicebench.md) |
| Nemotron 3 VoiceChat V1 | Earlier benchmark submission used an early-access release. The public NemotronLabs VoiceChat 11B is listed with an explicit distinction. [Coverage evidence](voicebench.md) |
| [DuplexSLA](https://github.com/hyzhang24/DuplexSLA) | The repository states that inference code and checkpoints are not yet released. A paper/training recipe alone is insufficient for inclusion. |
| [EmpathyOmni](https://github.com/W311411/Empathy-Omni) | The inspected README's checkpoint link is an empty placeholder; no actual author checkpoint was verified. |
| Other unreleased papers in the survey bibliographies | Remain discovery leads until actual code and weights are established; absence from the catalog does not mean no release can exist elsewhere. |

Restricted research releases and incomplete license declarations are visibly labeled in the catalog. They are not represented as unrestricted open source. Closed API products remain excluded. This audit establishes coverage of the pinned VoiceBench snapshot, not worldwide completeness.
