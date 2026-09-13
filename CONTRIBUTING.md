# Contributing a model

[← Model index](README.md#models)

The editable catalog is [data/models.json](data/models.json). The README, category lists and timeline are generated from it; edit the JSON first.

1. Check the [scope and counting rules](docs/methodology.md), including existing family names and variants. Disambiguate unrelated models that share a name.
2. Add a record with a stable lowercase hyphenated `id`, a display `name`, one `category`, input/output modality arrays, an `interaction` label, a short architecture description and capability notes.
3. Link primary evidence: the author paper, official repository, model card or vendor documentation. Record the source title, the actual review date and the review level. Do not assign claims based only on a community list or a model name.
4. Put related sizes, minor releases and aliases in `variants`. Explain restrictions when a family's capability columns span different checkpoints. Use an empty array when no variants are recorded.
5. Use null for both `source_date` and `source_date_kind` if no publication/announcement date was established. Do not turn an API snapshot suffix into a release date. Update the top-level `as_of` when adding evidence reviewed after the current snapshot.
6. Add a matching record to [data/figures.json](data/figures.json). Prefer a legible architecture or method figure from the same primary source. Store the PNG in `assets/architectures/`, record its original URL, figure number and SHA-256, and inspect the full image. If no suitable source figure is available, use `io-diagram`; the script generates a labeled SVG from the model's documented inputs and outputs.
7. Regenerate and check:

```bash
python3 scripts/catalog.py
python3 scripts/catalog.py --check
git diff --check
```

The script uses Python's standard library. It validates catalog metadata, one visual per model, figure provenance and checksums, generated content, and local links including images. A passing check does not replace reviewing the sources, inspecting figures or verifying a claimed model capability.

Every entry appears with its image in both the README and its category page. Keep the README card to one architecture sentence, source links and the credited image; capability notes and variants belong on the category page. The alphabetical README index links directly to these illustrated cards.

For a deeper architecture article, use the optional [model template](templates/model-template.md). Keep measured results tied to exact model versions and benchmark settings. Distinguish paper claims from reproduction results, code licenses from weights licenses, and native model outputs from external generators.

## Record fields

| Field | Meaning |
| --- | --- |
| `id` / `name` | Stable link anchor / human-readable model name. |
| `category` | `omni`, `dialogue`, `foundation`, `understanding`, `asr`, `generation` or `related`. |
| `inputs` / `outputs` | Arrays using T, I, V, A, S, M and X as defined in the methodology. |
| `interaction` | `text-output`, `generation`, `streaming`, `full-duplex`, `system` or `not-specified`. |
| `architecture` / `notes` | Concise design summary / capability scope and qualifications. |
| `variants` | Verified checkpoint, release or alias names, grouped where appropriate. |
| `source_date` / `source_date_kind` | YYYY-MM-DD and `paper` or `announcement`, or two nulls. |
| `sources` | Nonempty array of primary-source records. |
| `sources[].kind` | `paper`, `repository`, `model-card`, `documentation`, `announcement` or `project`. |
| `sources[].title` / `url` | Source title and direct HTTPS URL. |
| `sources[].reviewed_on` / `review_level` | Actual review date and scope of inspection; see the methodology. |

## Figure records

`data/figures.json` maps each model ID to one figure record. For `source-figure`, use a local `.png` path, a `source_url` already listed in the model record, the exact image or PDF `origin_url`, a concise `locator` such as `Figure 2, PDF p. 3`, and the local file's `sha256` checksum. Review the selected figure itself; a benchmark plot or logo is not an architecture diagram. Different generations need their own figure unless the source explicitly covers the family.

For `io-diagram`, use `assets/architectures/<model-id>.svg`, a primary `source_url`, `locator: "Input/output diagram"`, and null values for `origin_url` and `sha256`. The generated SVG summarizes the public interface without inferring internals. Keep third-party rights separate from repository licensing; see the [figure notice](assets/architectures/FIGURE_NOTICE.md).
