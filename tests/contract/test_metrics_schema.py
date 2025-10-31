import json, pathlib

def test_metrics_summary_sample_has_required_fields():
    p = pathlib.Path("samples/metrics_summary.sample.json")
    obj = json.loads(p.read_text())
    assert all(k in obj for k in ("mae","rmse","smape"))
