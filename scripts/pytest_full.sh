#!/usr/bin/env bash
set -euo pipefail
TS=$(date +%Y%m%d_%H%M%S)
PYTHONPATH="$(pwd)" pytest -n auto --maxfail=1 --reruns 1 \
  --html "reports/pytest_${TS}.html" --self-contained-html \
  --junitxml "reports/junit_${TS}.xml" \
  --json-report --json-report-file "reports/pytest_${TS}.json" \
  --cov=src --cov-report=term-missing --cov-report=html:"reports/coverage_${TS}" \
  -m "not slow"
echo "[ok] reports in reports/ (html/junit/json/coverage_${TS})"
