# tsf

**EN**: Reference scaffold for a reproducible, observable, extensible time-series forecasting system.
**JA**: 再現性・可観測性・拡張性を重視した時系列予測システムの参照スキャフォールド。

## Key Features / 主要機能
- Duplicate-run skip via fingerprint + DB uniqueness
- Rolling-origin backtest (expanding/rolling)
- DB=SoT, MLflow=Secondary (async sync)
- Typer CLI (fallback argparse here for smoke), Hydra configs (files provided), JSON Schemas
- Prometheus exporter + Grafana dashboards (provisioning)
- Alembic migrations (experiments/runs/metrics/artifacts/runs_ext)

See `RUNBOOK.md` for exact commands (JA/EN).

### Run fingerprint (stable & length-configurable)
- `RunManager.fingerprint()` returns a **64-char** SHA-256 of canonicalized cfg (cfg-only).
- `RunManager.compute_fingerprint(..., length=16)` returns a **short, stable ID** by default.
  Pass `length=64` for the full hash.
- Allowed lengths: even numbers in **[4, 64]**. Short IDs are **prefixes** of the 64-char hex.
