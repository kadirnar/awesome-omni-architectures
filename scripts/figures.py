"""Figure provenance, local asset checks and reproducible interface diagrams."""

from collections import Counter
from hashlib import sha256
from html import escape
from pathlib import Path
import re
import struct
import textwrap
from urllib.parse import urlsplit

MODALITY_NAMES = {
    "T": "Text", "I": "Images", "V": "Video", "A": "Audio",
    "S": "Speech", "M": "Music", "X": "Other modalities",
}


def validate_figures(catalog, manifest, root):
    models = {m["id"]: m for m in catalog["models"]}
    if manifest.get("schema_version") != 1 or set(manifest.get("models", {})) != set(models):
        raise ValueError("Figure manifest must contain exactly one record per model")
    required = {"kind", "path", "source_url", "origin_url", "locator", "sha256"}
    checked = set()
    for mid, figure in manifest["models"].items():
        if set(figure) != required or figure["kind"] not in {"source-figure", "io-diagram"}:
            raise ValueError(f"{mid}: invalid figure fields/kind")
        if figure["source_url"] not in {s["url"] for s in models[mid]["sources"]}:
            raise ValueError(f"{mid}: figure must cite one of the model's primary sources")
        path = Path(figure["path"])
        expected_suffix = ".svg" if figure["kind"] == "io-diagram" else ".png"
        if path.parent.as_posix() != "assets/architectures" or path.suffix != expected_suffix:
            raise ValueError(f"{mid}: invalid local figure path")
        if not figure["locator"].strip():
            raise ValueError(f"{mid}: missing figure locator")
        if figure["kind"] == "io-diagram":
            if path.name != f"{mid}.svg" or figure["origin_url"] is not None or figure["sha256"] is not None:
                raise ValueError(f"{mid}: interface diagrams must be generated locally")
            continue
        origin = urlsplit(figure["origin_url"])
        if origin.scheme != "https" or not origin.netloc or origin.username or origin.password or re.search(r"\s", figure["origin_url"]):
            raise ValueError(f"{mid}: invalid figure origin URL")
        if not re.fullmatch(r"[0-9a-f]{64}", figure["sha256"]):
            raise ValueError(f"{mid}: invalid asset checksum")
        signature = (figure["path"], figure["sha256"])
        if signature in checked:
            continue
        data = (root / path).read_bytes()
        if sha256(data).hexdigest() != figure["sha256"]:
            raise ValueError(f"{mid}: figure checksum mismatch")
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            raise ValueError(f"{mid}: figure is not a PNG")
        width, height = struct.unpack(">II", data[16:24])
        if width < 160 or height < 60:
            raise ValueError(f"{mid}: figure is too small to read")
        checked.add(signature)


def render_interface(model):
    """Show only documented input/output sets; do not infer internal connections."""
    name = escape(model["name"])
    title_lines = textwrap.wrap(model["name"], width=49)
    architecture = textwrap.wrap(model["architecture"], width=36)
    rows = max(len(model["inputs"]), len(model["outputs"]), 3)
    top = 112 + (len(title_lines) - 1) * 38
    body_height = max(rows * 46 + 50, 250)
    height = top + body_height + 82
    center = top + body_height / 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{name}: documented inputs and outputs</title>",
        "<desc id=\"desc\">Editorial interface diagram. Internal architecture and per-task modality combinations are not shown. See the model notes and primary sources.</desc>",
        '<rect width="1120" height="100%" rx="18" fill="#f8fafc"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        '<text x="42" y="33" font-size="13" font-weight="700" letter-spacing="2" fill="#64748b">DOCUMENTED INTERFACE · EDITORIAL DIAGRAM</text>',
    ]
    for index, title in enumerate(title_lines):
        parts.append(f'<text x="42" y="{76 + index * 38}" font-size="32" font-weight="700" fill="#0f172a">{escape(title)}</text>')
    parts += [
        f'<rect x="365" y="{center - 97}" width="390" height="194" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>',
        f'<text x="560" y="{center - 60}" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="2" fill="#64748b">MODEL / SYSTEM</text>',
    ]
    start = center - (len(architecture) - 1) * 13
    for index, line in enumerate(architecture):
        parts.append(f'<text x="560" y="{start + index * 26}" text-anchor="middle" font-size="19" font-weight="600" fill="#0f172a">{escape(line)}</text>')
    parts.append(f'<text x="560" y="{center + 67}" text-anchor="middle" font-size="14" fill="#64748b">{escape(model["interaction"])}</text>')
    for side, x, color in [("inputs", 42, "#0369a1"), ("outputs", 842, "#047857")]:
        values = model[side]
        parts.append(f'<text x="{x}" y="{top + 10}" font-size="13" font-weight="700" letter-spacing="2" fill="{color}">{side.upper()}</text>')
        first = center - (len(values) * 46 - 10) / 2
        for index, modality in enumerate(values):
            y = first + index * 46
            parts += [
                f'<rect x="{x}" y="{y}" width="236" height="36" rx="8" fill="#ffffff" stroke="#cbd5e1"/>',
                f'<text x="{x + 14}" y="{y + 24}" font-size="17" fill="{color}">{MODALITY_NAMES[modality]}</text>',
            ]
    parts += [
        f'<path d="M292 {center} H346 M337 {center - 7} L347 {center} L337 {center + 7}" fill="none" stroke="#0369a1" stroke-width="2.5"/>',
        f'<path d="M773 {center} H827 M818 {center - 7} L828 {center} L818 {center + 7}" fill="none" stroke="#047857" stroke-width="2.5"/>',
        f'<text x="42" y="{height - 37}" font-size="15" fill="#64748b">Input/output summary; internal architecture is not shown. Task and variant limits apply.</text>',
        "</g></svg>",
    ]
    return "\n".join(parts) + "\n"


def render_credits(models, manifest):
    figures = manifest["models"]
    counts = Counter(f["kind"] for f in figures.values())
    lines = [
        "# Figure credits", "",
        "<!-- Generated by scripts/catalog.py from data/models.json and data/figures.json. -->", "",
        f'{counts["source-figure"]} entries show a primary-source figure; {counts["io-diagram"]} use an editorial input/output diagram.', "",
        "Source figures belong to their authors or publishers; see the [figure notice](FIGURE_NOTICE.md). Shared family figures can appear in more than one model entry. Interface diagrams summarize catalog metadata and do not reconstruct undisclosed internals.", "",
        "| Model | Visual | Primary source | Image origin |", "| --- | --- | --- | --- |",
    ]
    for model in models:
        figure = figures[model["id"]]
        origin = f'[Original]({figure["origin_url"]})' if figure["origin_url"] else "Generated from catalog"
        lines.append(f'| {model["name"]} | [{figure["locator"]}]({Path(figure["path"]).name}) | [Source]({figure["source_url"]}) | {origin} |')
    return "\n".join(lines) + "\n"
