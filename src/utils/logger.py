from __future__ import annotations
import json, sys, time, uuid
from typing import Any, Dict

def json_log(level: str, message: str, **fields: Any) -> None:
    rec = {"ts": time.time(), "level": level, "msg": message, **fields}
    sys.stdout.write(json.dumps(rec, ensure_ascii=False) + "\n")
    sys.stdout.flush()

def new_ids() -> Dict[str, str]:
    return {"run_id": uuid.uuid4().hex[:8], "request_id": uuid.uuid4().hex[:8]}
