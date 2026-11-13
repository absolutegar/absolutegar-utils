import hashlib
import hmac
from typing import Dict, Any

class CryptoHandler:
    def __init__(self, secret: str):
        self.secret = secret.encode('utf-8')

    def generate_signature(self, payload: str) -> str:
        return hmac.new(
            self.secret, 
            payload.encode('utf-8'), 
            hashlib.sha256
        ).hexdigest()

    def validate_payload(self, payload: str, signature: str) -> bool:
        expected = self.generate_signature(payload)
        return hmac.compare_digest(expected, signature)

    @staticmethod
    def sanitize_data(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: str(v).strip() for k, v in data.items() if v is not None}

    def process_order(self, order_data: Dict[str, Any], signature: str) -> bool:
        serialized = str(order_data)
        if not self.validate_payload(serialized, signature):
            return False
        
        cleaned = self.sanitize_data(order_data)
        return 'price' in cleaned and 'quantity' in cleaned