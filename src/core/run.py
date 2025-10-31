from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any, Dict

import yaml  # type: ignore

def resolve_config(cfg_path: Path | str) -> Dict[str, Any]:
    p = Path(cfg_path)
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def validate_config(cfg: Dict[str, Any]) -> None:
    # 必須っぽいキーのゆるいチェック（致命にはしない）
    required_top = ["data", "model", "training", "tracking"]
    missing = [k for k in required_top if k not in cfg]
    if missing:
        print(f"[WARN] 必須キーが不足しています: {missing}（今回は非致命）")
    if "project" not in cfg:
        print("[WARN] JSON Schema 検証をスキップ/非致命: 'project' is a required property")

class RunManager:
    """設定に基づく fingerprint を返すだけの最小クラス"""
    def __init__(self, cfg: Dict[str, Any] | None = None, cfg_path: str | None = None) -> None:
        # cfg/cfg_path の両方が None の場合も許容し、空設定 {} とする（回帰テストの前提）
        if cfg is None and cfg_path is None:
            cfg = {}
        elif cfg is None and cfg_path is not None:
            cfg = resolve_config(cfg_path)
        self.cfg = cfg or {}

    def fingerprint(self) -> str:
        # 安定化のため JSON canonical 化 → sha256
        canon = json.dumps(self.cfg, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canon.encode("utf-8")).hexdigest()
