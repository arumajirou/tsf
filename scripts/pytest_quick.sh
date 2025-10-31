#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH="$(pwd)" pytest -q -n auto -m "unit or smoke" -ra \
  --maxfail=1 --reruns 1 \
  --json-report --json-report-file "reports/quick.json"
