from src.core.run import RunManager

def test_empty_cfg_fingerprint_is_stable():
    m = RunManager(None)
    assert m.fingerprint() == "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
