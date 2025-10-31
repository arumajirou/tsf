# tsf (EN/JA)

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
