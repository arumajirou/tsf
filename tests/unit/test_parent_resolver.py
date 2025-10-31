from src.core.parent_resolver import PrefixResolver

def test_prefix_resolver_basic():
    r = PrefixResolver(prefix="PARENT:")
    assert r.is_parent("PARENT:GLOBAL")
    assert not r.is_parent("STORE_001")
    assert r.parent_key("STORE_001") == "STORE"
