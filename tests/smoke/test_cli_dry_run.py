import subprocess, sys

def test_cli_train_dry_run():
    cmd = [sys.executable, "-m", "src.runner.cli", "train", "--dry-run", "--config", "conf/config.yaml"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert res.returncode == 0
    assert "train end" in res.stdout.lower()
