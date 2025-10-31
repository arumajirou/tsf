from __future__ import annotations
class PrefixResolver:
    def __init__(self, prefix: str = "PARENT:") -> None:
        self.prefix = prefix
    def is_parent(self, uid: str) -> bool:
        return uid.startswith(self.prefix)
    def parent_key(self, uid: str) -> str:
        return uid.split("_")[0]
