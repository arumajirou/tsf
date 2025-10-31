from pathlib import Path
import textwrap, yaml
from src.core.run import resolve_config

def test_resolve_config_roundtrip(tmp_path):
    cfg = {
        "project": {"name": "tsf", "version": "0.1.0"},
        "data": {"path": "./samples/data.csv"},
        "model": {"name": "NHITS"},
        "training": {"epochs": 1}
    }
    p = tmp_path / "cfg.yaml"
    p.write_text(yaml.safe_dump(cfg, sort_keys=True))
    loaded = resolve_config(str(p))
    assert loaded["project"]["name"] == "tsf"
    assert loaded["model"]["name"] == "NHITS"
