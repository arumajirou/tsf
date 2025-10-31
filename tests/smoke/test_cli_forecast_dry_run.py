import sys, subprocess

def test_cli_forecast_dry_run():
    cmd = [sys.executable, "-m", "src.runner.cli", "forecast", "--dry-run", "--config", "conf/config.yaml"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert res.returncode == 0
    assert "forecast end" in res.stdout.lower()
