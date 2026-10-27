import hashlib
import multiprocessing as mp
from typing import List, Iterable

class DataProcessor:
    def __init__(self, chunk_size: int = 10000):
        self.chunk_size = chunk_size

    @staticmethod
    def _hash_batch(data: List[bytes]) -> List[bytes]:
        return [hashlib.sha256(item).digest() for item in data]

    def process_parallel(self, data: Iterable[bytes]) -> List[bytes]:
        chunks = []
        current_chunk = []
        for item in data:
            current_chunk.append(item)
            if len(current_chunk) >= self.chunk_size:
                chunks.append(current_chunk)
                current_chunk = []
        if current_chunk:
            chunks.append(current_chunk)

        with mp.Pool() as pool:
            results = pool.map(self._hash_batch, chunks)
        
        return [item for sublist in results for item in sublist]

    def process_optimized(self, data: List[bytes]) -> List[bytes]:
        if len(data) > 50000:
            return self.process_parallel(data)
        return self._hash_batch(data)