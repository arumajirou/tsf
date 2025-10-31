# RUNBOOK (EN/JA)

## EN
### Environment
- Python: 3.11.14 (conda env: nc)
- CUDA: 13.0, Torch: 2.9.0+cu130
- OS: Ubuntu Linux 6.14.0-35-generic

### Commands (exact)
```bash
# 1) PostgreSQL (local test; adjust privileges as needed)
sudo systemctl enable --now postgresql || true
sudo -u postgres createuser $USER -s || true
createdb ts_db || true

# 2) Use existing conda env 'nc'
conda activate nc
python -V

# 3) Install deps (torch already installed)
pip install -r requirements.txt --no-deps

# 4) DB migration (requires alembic/psycopg2)
alembic upgrade head

# 5) Dry-run training (no side effects)
python -m runner.cli train --dry-run --config conf/config.yaml

# 6) Smoke tests (≤5min)
pytest -q -m "not slow" --maxfail=1

# 7) Backtest sample
python -m runner.cli backtest --config conf/config.yaml --apply

# 8) Exporter/Grafana (docker compose)
docker compose up -d prometheus grafana
```

### Rollback
```bash
alembic downgrade -1
docker compose down -v
git restore . && git clean -fd
```

## JA
### 環境
- Python: 3.11.14（conda: nc）
- CUDA: 13.0 / Torch: 2.9.0+cu130
- OS: Ubuntu Linux 6.14.0-35-generic

### 手順（厳密コマンド）
上記 EN セクションと同一。詳細は README と ADR を参照。
