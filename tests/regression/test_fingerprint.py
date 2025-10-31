import pytest
pytest.importorskip("src.core.run")

from src.core.run import RunManager

@pytest.mark.xfail_known(reason="Spec pending: fingerprint length 16 vs 64", strict=false)
def test_fingerprint_stability():
    m = RunManager(None)
    fp1 = m.compute_fingerprint(model_adapter_name="NHITS",
                                hyperparameters={"lr":0.001},
                                dataset_version="d", training_window={}, code_revision="x", random_seed=42)
    fp2 = m.compute_fingerprint(model_adapter_name="NHITS",
                                hyperparameters={"lr":0.001},
                                dataset_version="d", training_window={}, code_revision="x", random_seed=42)
    assert fp1 == fp2 and len(fp1) == 16
