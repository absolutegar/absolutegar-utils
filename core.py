import hashlib
from functools import lru_cache
from typing import List, Sequence


class FastBatchHasher:
    __slots__ = ("_cache_size",)

    def __init__(self, cache_size: int = 8192) -> None:
        self._cache_size = cache_size

    @staticmethod
    @lru_cache(maxsize=8192)
    def double_sha256(data: bytes) -> bytes:
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    def compute_merkle_root(self, leaf_hashes: Sequence[bytes]) -> bytes:
        if not leaf_hashes:
            return b""
        current_level = list(leaf_hashes)
        while len(current_level) > 1:
            if len(current_level) % 2 != 0:
                current_level.append(current_level[-1])
            next_level = []
            for i in range(0, len(current_level), 2):
                combined = current_level[i] + current_level[i + 1]
                next_level.append(self.double_sha256(combined))
            current_level = next_level
        return current_level[0]

    def batch_double_sha256(self, payloads: Sequence[bytes]) -> List[bytes]:
        return [self.double_sha256(p) for p in payloads]
