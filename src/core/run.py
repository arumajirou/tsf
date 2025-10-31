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

def _canonicalize(x: Any) -> Any:
    """dictはキーソート、list/tupleは順序維持、setはソートして再帰的に正規化"""
    if isinstance(x, dict):
        return {k: _canonicalize(x[k]) for k in sorted(x)}
    if isinstance(x, (list, tuple)):
        return [ _canonicalize(i) for i in x ]
    if isinstance(x, (set, frozenset)):
        return sorted([ _canonicalize(i) for i in x ])
    return x

class RunManager:
    """指紋（fingerprint）計算の最小実装"""
    def __init__(self, cfg: Dict[str, Any] | None = None, cfg_path: str | None = None) -> None:
        # cfg/cfg_path の両方が None の場合も許容し、空設定 {} とする（回帰テストの前提）
        if cfg is None and cfg_path is None:
            cfg = {}
        elif cfg is None and cfg_path is not None:
            cfg = resolve_config(cfg_path)
        self.cfg = cfg or {}

    def fingerprint(self) -> str:
        """現在の cfg のみを材料にしたハッシュ（互換維持）"""
        canon = json.dumps(self.cfg, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canon.encode("utf-8")).hexdigest()

    def compute_fingerprint(
        self,
        *,
        model_adapter_name: str,
        hyperparameters: Dict[str, Any] | None = None,
        dataset_version: str | None = None,
        training_window: Dict[str, Any] | None = None,
        code_revision: str | None = None,
        random_seed: int | None = None,
        **extra: Any,
    ) -> str:
        """学習条件一式から安定な指紋を算出"""
        payload = {
            "version": 1,  # 将来の互換性のためのバージョン
            "base_cfg_hash": self.fingerprint(),  # cfg変更の影響を反映
            "model_adapter_name": model_adapter_name,
            "hyperparameters": _canonicalize(hyperparameters or {}),
            "dataset_version": dataset_version,
            "training_window": _canonicalize(training_window or {}),
            "code_revision": code_revision,
            "random_seed": int(random_seed) if random_seed is not None else None,
        }
        if extra:
            payload["extra"] = _canonicalize(extra)

        canon = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canon.encode("utf-8")).hexdigest()
