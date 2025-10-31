import subprocess, sys
def test_cli_help_runs():
    r = subprocess.run([sys.executable,"-m","src.runner.cli","--help"],capture_output=True,text=True,timeout=60)
    assert r.returncode==0
    assert "run" in r.stdout and "train" in r.stdout
