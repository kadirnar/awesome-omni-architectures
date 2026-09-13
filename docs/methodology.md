# Scope and evidence

[← Model list](../README.md#models)

This catalog includes open-source omni model releases with public implementations, downloadable checkpoints and separately verified code and weight licenses. Each entry has a language-model backbone and documented visual and audio inputs. Models that generate only text can qualify; speech output is recorded separately.

## Inclusion

A release must have all of the following:

- An official implementation, either in the author's code repository or in the published checkpoint repository.
- Publicly downloadable model weights, with a named checkpoint and a recorded revision.
- Explicit open licenses for both the implementation and weights, supported by license text, source-file headers or a publisher's release declaration.
- Documented text, visual and audio inputs, plus a primary source for its architecture.

API-only products, paper-only proposals, standalone speech/TTS/ASR models, visual-only models and modular systems without their own qualifying omni checkpoint are excluded. Research-only, non-commercial and ambiguously licensed releases are also excluded. A public repository or an “open” model name does not establish an open license.

License badges are checked against the accompanying terms. Conflicting or additional usage restrictions prevent inclusion until clarified by the publisher. The code and weight licenses can differ; both are shown on every card. The selected checkpoint is the verified release, and other sizes or family members do not automatically inherit its license or capabilities.

Here, open-source describes the code and weight release. The catalog does not certify the openness of the complete training pipeline or training datasets. Training data, third-party components and architecture figures can have separate licenses.

## Modalities and interaction

| Symbol | Meaning |
| --- | --- |
| T | Text, including prompts and transcripts |
| I / V | Images / video, which may be processed as sampled frames |
| A / S / M | General audio / speech / music |
| X | Other structured modalities, detailed in the model notes |

Input/output sets summarize documented capabilities, not every possible combination. `text-output` means the model responds in text. `generation` makes no latency claim; `streaming` requires documented incremental processing or output. `full-duplex` requires explicit support for concurrent listening and speaking. `not-specified` retains uncertainty.

## Sources and dates

Papers, official repositories, checkpoint cards and publisher documentation support the entries. `sources[].review_level` records whether the reviewed material was an abstract, README, model card, documentation, announcement or project page. License evidence is linked separately in `release`, with the checkpoint revision and review date.

`source_date` is the first paper submission or a verified dated announcement, not necessarily the checkpoint release date. An older paper can describe a family with a later open release. The [timeline](timeline.md) retains those paper dates; unknown dates remain blank. Repository activity and API version suffixes are not release dates.

No model weights were downloaded for this review. Public checkpoint file listings and license declarations were inspected; model inference, benchmark results and latency were not reproduced. Automated checks verify metadata and links offline, while source availability and licensing require renewed primary-source review.

## Figures and maintenance

Every entry has a local figure in both the README and [model details](../models/omni.md). [Figure credits](../assets/architectures/CREDITS.md) retain the primary source, original image/PDF URL and figure locator. Family figures are identified in the notes when the verified checkpoint is a later release. Labeled input/output diagrams summarize documented interfaces without inventing internal architecture.

The repository license does not relicense third-party figures; see the [figure notice](../assets/architectures/FIGURE_NOTICE.md).

[data/models.json](../data/models.json) and [data/figures.json](../data/figures.json) are the sources of truth. The generator requires omni inputs, code/weight license evidence and one visual per entry. See [CONTRIBUTING.md](../CONTRIBUTING.md) for updates.
