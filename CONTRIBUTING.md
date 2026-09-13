# Contributing an open-source omni model

[← Model list](README.md#models)

Add a model only after verifying its official implementation, downloadable checkpoint and open code/weight licenses. It must accept text, visual and audio inputs. Follow the [scope](docs/methodology.md); API-only, speech-only, research-only and unlicensed releases do not qualify.

1. Edit [data/models.json](data/models.json), using schema version 2 and an existing entry as the template. Keep a stable ID, category `omni`, concise architecture/notes, verified modalities and primary sources.
2. Add the `release` record below. Read the actual terms and source headers as well as license badges. Resolve restrictions or conflicting license claims before inclusion. List only verified checkpoint variants.
3. Add a corresponding record to [data/figures.json](data/figures.json). Prefer an appropriate primary-source figure with its original URL, locator and SHA-256. Use a labeled `io-diagram` when no suitable source figure is available.
4. Regenerate and validate:

   ```bash
   python3 scripts/catalog.py
   python3 scripts/catalog.py --check
   git diff --check
   ```

Every model must appear with its image, code, weights and license links in the README and its detail page. Keep longer qualifications in the detail page. Inspect rendered Markdown and any new or changed figures before sharing.

## Release evidence

| Field | Required evidence |
| --- | --- |
| `checkpoint` | Exact publisher/checkpoint identifier for the reviewed weights |
| `code_url` | Official model implementation; a demo that only calls an external API is insufficient |
| `weights_url` | Public checkpoint repository containing actual weight files |
| `code_license` / `weights_license` | Separately reviewed license identifiers |
| `code_license_url` / `weights_license_url` | Primary license text, source header or explicit publisher declaration |
| `weights_revision` | Full commit hash of the inspected checkpoint repository |
| `reviewed_on` | Date the release evidence was inspected |

All four evidence URLs must also appear in the entry's `sources`, with a title, kind, review date and review level. Use an existing supported open license identifier; extend the validator only after reviewing an additional license. Do not substitute a repository's code license for the model's weight terms.

The generator uses Python's standard library. It validates scope, release metadata, primary-source URLs, dates, figure checksums, local links, anchors and generated-file consistency. It does not automatically verify remote availability or certify license claims.

Source dates refer to papers or explicit announcements. Keep unknown dates null. Source figures retain their own rights; see the [figure notice](assets/architectures/FIGURE_NOTICE.md). Optional longer articles can use the [model template](templates/model-template.md).
