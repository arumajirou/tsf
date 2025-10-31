#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

TS="$(date +%Y%m%d_%H%M%S)"
OUT=reports
HTML="${OUT}/pytest_${TS}.html"
JUNIT="${OUT}/junit_${TS}.xml"
JSON="${OUT}/pytest_${TS}.json"
COV_DIR="${OUT}/coverage_${TS}"

mkdir -p "${OUT}" "${COV_DIR}"

PYTHONPATH="$(pwd):${PYTHONPATH:-}" \
pytest -n auto --maxfail=1 --color=yes \
  --reruns 1 --reruns-delay 2 \
  --html "${HTML}" --self-contained-html \
  --junitxml "${JUNIT}" \
  --json-report --json-report-file "${JSON}" \
  --cov=src --cov-report=term-missing --cov-report=html:"${COV_DIR}"

echo "[OK] Reports:"
ls -1 "${OUT}" | sed -n '1,50p'
echo "[HINT] Coverage HTML: ${COV_DIR}/index.html"
