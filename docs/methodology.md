# Scope and evidence

[← Model list](../README.md#models)

The catalog covers publicly released omni, speech and audio **language models**, including the open releases evaluated by VoiceBench. Each model needs public implementation code, an actual checkpoint and a short explanation of its purpose. API-only products and unreleased paper proposals are excluded from the model cards.

## Collections

| Collection | Scope |
| --- | --- |
| Omni | Text, visual and audio inputs; output may be text only or multimodal |
| Speech | Speech/audio input and spoken output, including full-duplex dialogue and simultaneous translation |
| Audio | Audio-to-text understanding, reasoning, spoken instructions and speech-language interaction controllers |
| LLM-ASR | Speech recognition models built around a language-model backbone |
| Cascade | VoiceBench baselines composed of separately released ASR and text LLM checkpoints |

Text-only LLMs, visual-only VLMs, standalone audio encoders/codecs and pure text-to-speech generators are outside this catalog. An ASR checkpoint appears as a separate component when required to reproduce a VoiceBench cascade. Systems with their own trained speech-dialogue controller, such as DuplexCascade, are described as systems in their model notes.

## Release and license labels

A public repository or a benchmark's “Open” flag does not establish an open-source license. Code and weight terms are checked separately, including model-card body text and inherited base-model conditions.

| Label | Meaning |
| --- | --- |
| Open license | Explicit open licenses found for the reviewed code and checkpoint |
| Custom / restricted | Public code and weights with custom, research-only, noncommercial or base-model conditions; these are not presented as unrestricted open-source releases |
| License unclear | Code and actual weights are public, but a complete license declaration was not located; inclusion is a research record, not permission to use them |

The expanded scope includes LFM's custom-licensed public audio models and distinguishes restricted or unclear VoiceBench releases. Missing licenses are never filled in from a related model. A conflicting restrictive declaration overrides a permissive metadata badge for catalog classification. Each card links to the evidence and states the limitation briefly.

Checkpoint repositories are inspected for actual weight files, and their exact revisions are recorded. For author-hosted archives without repository commits, an explicitly labeled HTTP ETag is retained; it is not a cryptographic checksum or an immutable URL. Normal public access gates requiring acceptance of published terms are identified in the notes. A demo that only calls a hosted API is insufficient. The [VoiceBench audit](voicebench.md) records exact benchmark checkpoints that could not be verified without substituting a different release.

“Open license” concerns the reviewed code and weights; it does not certify open training data or the entire training process. Separately downloaded codecs, speech decoders and other dependencies retain their own terms.

## Modalities and interaction

| Symbol | Meaning |
| --- | --- |
| T | Text, including prompts and transcripts |
| I / V | Images / video, possibly sampled frames |
| A / S / M | General audio / speech / music |
| X | Other structured modalities, explained in the notes |

Input/output sets summarize supported interfaces, not every possible task combination. `text-output` means text responses. `generation` makes no latency claim. `streaming` requires documented incremental processing or output. `full-duplex` requires concurrent listening and speaking; a benchmark wrapper's label alone is insufficient. `not-specified` retains uncertainty.

Each entry selects a named checkpoint. Distinct benchmark releases, backbones, reasoning modes or language adaptations may have separate cards. Routine quantizations, mirrors and repeated size variants do not inflate the model count. Other family members do not automatically inherit the selected release's capabilities or license.

## Sources and dates

Primary papers, repositories, checkpoint cards and publisher documentation support the entries. `review_level` distinguishes abstracts, inspected paper sections, READMEs and model cards. See the [research trail](research.md).

`source_date` is a verified paper or announcement date, **not a checkpoint release date**. Family papers may predate later variants; dates for variants remain blank unless established separately. Repository activity and model-name suffixes are not used to guess release dates.

No model weights were downloaded or executed. Checkpoint file listings, implementation files and release declarations were inspected; benchmark scores and latency were not reproduced. Offline checks validate schema, release evidence, VoiceBench mappings, figures, links and generated-file consistency. They do not certify licensing or future remote availability.

## Figures and maintenance

Every entry has a local image in the README and its collection page. Prefer a relevant architecture or method figure from the authors. Shared family figures are labeled. When a suitable author figure is unavailable, an editorial input/output SVG describes the documented interface without inventing internal connections.

[Figure credits](../assets/architectures/CREDITS.md) record the primary source, original image URL, locator and checksum. Third-party figures retain their own rights under the [figure notice](../assets/architectures/FIGURE_NOTICE.md).

The source files are [models.json](../data/models.json), [figures.json](../data/figures.json) and [voicebench.json](../data/voicebench.json). See [CONTRIBUTING.md](../CONTRIBUTING.md) for updates. This is a dated, maintained catalog, not a claim that every model worldwide has been found.
