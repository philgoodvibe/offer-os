#!/usr/bin/env python3
"""
Offer OS — shared business-profile loader + data-adapter interface.

This is the portability layer. Skills NEVER hardcode a business or a data store;
they call `load_profile()` for the business config and use a `DataAdapter` for any
external reads/writes. A stranger runs everything with just `business-profile.yaml`
filled in (LocalFilesAdapter). Power users swap in a richer adapter (e.g. a CRM or
the Philgood Brain) without touching the skills.

Only dependency: PyYAML (pip install pyyaml). If you'd rather stay dependency-free,
save your profile as JSON and use load_profile(path='business-profile.json').
"""
from __future__ import annotations
import json, os
from pathlib import Path

def _find_profile(start: str | None = None) -> Path:
    here = Path(start or os.getcwd())
    for d in [here, *here.parents]:
        for name in ("business-profile.yaml", "business-profile.yml", "business-profile.json"):
            p = d / name
            if p.exists():
                return p
    # fall back to the shipped example so skills can still demo
    return Path(__file__).resolve().parent.parent / "business-profile.example.yaml"

def load_profile(path: str | None = None) -> dict:
    p = Path(path) if path else _find_profile()
    text = p.read_text()
    if p.suffix == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "PyYAML not installed. Run `pip install pyyaml`, or save your profile as "
            "business-profile.json and pass it to load_profile()."
        ) from e
    return yaml.safe_load(text)


class DataAdapter:
    """Interface every skill uses for external data. Default impl = local files.
    Implement these four methods to wire Offer OS into any system."""
    def get_transcripts(self) -> list[dict]:
        """Return [{'title','text','date'}...] of source recordings/notes."""
        raise NotImplementedError
    def get_past_offers(self) -> list[dict]:
        """Return prior offers/campaigns for reuse and benchmarking."""
        raise NotImplementedError
    def save_asset(self, kind: str, name: str, content: str) -> str:
        """Persist a generated asset; return where it landed."""
        raise NotImplementedError
    def save_record(self, table: str, row: dict) -> dict:
        """Persist a structured record (offer, problem-statement, audit). Return it."""
        raise NotImplementedError


class LocalFilesAdapter(DataAdapter):
    """Zero-infrastructure default. Reads transcripts from a folder, writes assets to disk."""
    def __init__(self, profile: dict | None = None):
        self.profile = profile or load_profile()
        data = (self.profile.get("data") or {})
        self.tx_dir = Path(data.get("transcripts_dir", "./inputs/transcripts"))
        self.out_dir = Path(data.get("assets_out_dir", "./outputs"))

    def get_transcripts(self) -> list[dict]:
        out = []
        if self.tx_dir.exists():
            for f in sorted(self.tx_dir.glob("*")):
                if f.is_file():
                    out.append({"title": f.stem, "text": f.read_text(errors="ignore"), "date": None})
        return out

    def get_past_offers(self) -> list[dict]:
        return self.profile.get("offers", [])

    def save_asset(self, kind: str, name: str, content: str) -> str:
        self.out_dir.mkdir(parents=True, exist_ok=True)
        p = self.out_dir / f"{kind}__{name}"
        p.write_text(content)
        return str(p)

    def save_record(self, table: str, row: dict) -> dict:
        self.out_dir.mkdir(parents=True, exist_ok=True)
        p = self.out_dir / f"{table}.jsonl"
        with p.open("a") as f:
            f.write(json.dumps(row) + "\n")
        return row


def get_adapter(profile: dict | None = None) -> DataAdapter:
    profile = profile or load_profile()
    kind = ((profile.get("data") or {}).get("adapter") or "local").lower()
    if kind == "local":
        return LocalFilesAdapter(profile)
    # 'brain' or other adapters are user-supplied overlays; fall back to local if absent.
    raise SystemExit(
        f"Adapter '{kind}' is not bundled. Offer OS ships the 'local' adapter only; "
        "provide your own DataAdapter subclass for '{kind}', or set data.adapter: local."
    )


if __name__ == "__main__":
    pr = load_profile()
    print("Loaded profile for:", pr.get("business", {}).get("name", "(unnamed)"))
    print("Destination:", pr.get("destination"))
    print("Adapter:", (pr.get("data") or {}).get("adapter", "local"))
