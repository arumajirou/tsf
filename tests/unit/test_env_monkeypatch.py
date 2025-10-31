import os

def test_env_monkeypatch(monkeypatch):
    monkeypatch.setenv("TSF_DUMMY_FLAG", "1")
    assert os.getenv("TSF_DUMMY_FLAG") == "1"
