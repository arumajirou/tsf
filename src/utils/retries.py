from __future__ import annotations
import random, time
from typing import Callable, Type, Tuple

def with_retries(fn: Callable, exceptions: Tuple[Type[BaseException], ...], tries: int = 3, base: float = 0.2) -> Callable:
    def wrapper(*args, **kwargs):
        for i in range(tries):
            try:
                return fn(*args, **kwargs)
            except exceptions as e:
                if i == tries - 1:
                    raise
                time.sleep(base * (2 ** i) + random.random() * 0.05)
    return wrapper
