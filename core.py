import hashlib
from functools import lru_cache
from typing import List, Tuple


@lru_cache(maxsize=2048)
def fast_double_sha256(payload: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(payload).digest()).digest()


class CoreCryptoProcessor:
    """Optimized cryptographic payload and merkle tree processor."""

    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    @staticmethod
    def hash_payload(data: bytes) -> bytes:
        return fast_double_sha256(data)

    def build_merkle_root(self, leaf_hashes: List[bytes]) -> bytes:
        if not leaf_hashes:
            return b""

        nodes = list(leaf_hashes)
        while len(nodes) > 1:
            if len(nodes) % 2 == 1:
                nodes.append(nodes[-1])
            nodes = [
                fast_double_sha256(nodes[i] + nodes[i + 1])
                for i in range(0, len(nodes), 2)
            ]
        return nodes[0]

    def process_batch(self, payloads: List[bytes]) -> List[Tuple[bytes, bytes]]:
        return [(fast_double_sha256(p), p) for p in payloads]
