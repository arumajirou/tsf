from pathlib import Path

# ParentResolver があれば使う（無ければ無視して続行）
try:
    from src.core.parent_resolver import ParentResolver  # type: ignore
except Exception:
    ParentResolver = None  # fallback


def resolve_config(config_path: "Path | str") -> dict:
    import yaml  # type: ignore
    p = Path(config_path)
    data = yaml.safe_load(p.read_text()) or {}

    if ParentResolver is not None:
        try:
            resolver = ParentResolver()
            data = resolver.resolve(data)
        except Exception:
            # resolver 未実装/不一致でも致命にしない
            pass

    data.setdefault("name", "time_series_forecasting")
    return data


def validate_config(cfg: dict) -> None:
    # まず必須キーの簡易チェック
    required_top = ("data", "model", "training")
    missing = [k for k in required_top if k not in cfg]
    if missing:
        raise ValueError(f"設定の必須キーが不足しています: {missing}")

    # 任意: JSON Schema による検証（失敗しても警告）
    try:
        import json, sys
        from jsonschema import validate  # type: ignore
        root = Path(__file__).resolve().parents[2]  # プロジェクトルート
        schema_path = root / "schemas" / "resolved_config.schema.json"
        if schema_path.exists():
            schema = json.loads(schema_path.read_text())
            validate(instance=cfg, schema=schema)
    except Exception as e:
        print(f"[WARN] JSON Schema 検証をスキップ/非致命: {e}", file=sys.stderr)
