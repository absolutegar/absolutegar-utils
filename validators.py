from typing import List, Tuple
import hashlib

def validate_batch(transactions: List[str], target: bytes) -> List[bool]:
    return [hashlib.sha256(tx.encode()).digest() == target for tx in transactions]

def batch_hash_verification(data: List[str], threshold: bytes) -> bool:
    results = validate_batch(data, threshold)
    return all(results)

class HashValidator:
    __slots__ = ('cache',)
    
    def __init__(self):
        self.cache = {}

    def check_integrity(self, tx_id: str, payload: str) -> bool:
        if tx_id in self.cache:
            return self.cache[tx_id]
        
        is_valid = hashlib.sha256(payload.encode()).hexdigest() == tx_id
        self.cache[tx_id] = is_valid
        return is_valid

def fast_verify_sequence(sequence: List[Tuple[str, str]]) -> bool:
    validator = HashValidator()
    return all(validator.check_integrity(tid, p) for tid, p in sequence)