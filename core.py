import hashlib
import hmac
from typing import Optional

class CryptoProcessor:
    def __init__(self, secret: str):
        self._secret = secret.encode()

    def generate_signature(self, payload: str) -> str:
        return hmac.new(
            self._secret,
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

    def verify_signature(self, payload: str, signature: str) -> bool:
        expected = self.generate_signature(payload)
        return hmac.compare_digest(expected, signature)

class DataSanitizer:
    @staticmethod
    def format_address(address: str) -> str:
        if not address:
            raise ValueError("invalid address")
        return address.lower().strip()

def process_transaction(payload: str, secret: str, signature: str) -> Optional[dict]:
    processor = CryptoProcessor(secret)
    if not processor.verify_signature(payload, signature):
        return None
    return {"status": "verified", "data": payload}
