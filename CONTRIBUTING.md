# Contributing a model

[← Model list](README.md#models)

Verify public implementation code, actual checkpoint files, documented audio input and a primary architecture source. Follow the [scope and license labels](docs/methodology.md). API-only and unreleased proposals belong in the research audit, not the model cards.

1. Add an entry to [data/models.json](data/models.json), schema version 3. Use the appropriate collection and a stable ID. Write one short `summary` explaining **what it does**, then a concise `architecture` and any necessary qualifications in `notes`.
2. Record the exact checkpoint and revision. Check code and weight licenses separately; read the terms beyond metadata badges. Use `open-license`, `restricted` or `unclear`, with a visible `license_notes` explanation for the latter two. Do not call restricted or unlicensed releases open-source.
3. Add a record to [data/figures.json](data/figures.json). Prefer a relevant author figure with source, original URL, locator and SHA-256. Otherwise use a generated, labeled `io-diagram`. Label shared family figures accurately.
4. Update [data/voicebench.json](data/voicebench.json) when changing benchmark coverage. Every Open row in the pinned snapshot needs an exact catalog mapping or an evidenced explanation. Closed rows stay excluded.
5. Regenerate and check:

   ```bash
   python3 scripts/catalog.py
   python3 scripts/catalog.py --check
   git diff --check
   ```

Inspect rendered Markdown and new figures. Keep README descriptions short; put details in collection pages. Do not count quantization copies as new models.

## Release evidence

| Field | Evidence |
| --- | --- |
| `checkpoint`, `weights_url`, `weights_revision` | Exact publisher checkpoint, actual weight files and inspected repository commit (or documented archive HTTP ETag) |
| `code_url` | Public implementation, including the correct branch or upstream model module |
| `code_license`, `weights_license` | Separately reviewed terms; use `Not stated` rather than guessing |
| `code_license_url`, `weights_license_url` | License text, source header or explicit publisher declaration; model card for missing weight terms |
| `reviewed_on`, `status`, `license_notes` | Review date, license classification and any restrictions or uncertainty |
| `components` | Empty for a model; cascades list additional ASR checkpoint, license and revision |

All evidence URLs must also appear in `sources`. Preserve source dates only when established by a paper or dated announcement. Do not substitute a code license for weight terms or a related checkpoint for an unreleased benchmark submission.

The generator uses only Python's standard library. Validation checks metadata and local consistency; primary-source research remains necessary. The [model template](templates/model-template.md) is available for longer articles.
