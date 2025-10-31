import json, random
from copy import deepcopy
from hypothesis import given, strategies as st
from src.core.run import RunManager

@st.composite
def small_dict(draw):
    keys = st.text(min_size=1, max_size=5)
    vals = st.one_of(st.integers(min_value=-5, max_value=5), st.floats(allow_nan=False, allow_infinity=False, width=32), st.text(min_size=0, max_size=8))
    return draw(st.dictionaries(keys, vals, min_size=0, max_size=5))

@given(hp=small_dict(), tw=small_dict())
def test_compute_fingerprint_is_order_insensitive(hp, tw):
    rm = RunManager({})
    # 同じ内容で挿入順だけシャッフル
    items = list(hp.items())
    random.Random(42).shuffle(items)
    hp_shuffled = dict(items)
    fp1 = rm.compute_fingerprint(model_adapter_name="NHITS",
                                 hyperparameters=hp,
                                 dataset_version="d",
                                 training_window=tw,
                                 code_revision="x",
                                 random_seed=123)
    fp2 = rm.compute_fingerprint(model_adapter_name="NHITS",
                                 hyperparameters=hp_shuffled,
                                 dataset_version="d",
                                 training_window=deepcopy(tw),
                                 code_revision="x",
                                 random_seed=123)
    assert fp1 == fp2
