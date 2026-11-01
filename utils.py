import hashlib
import hmac
from typing import Any, Dict

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def normalize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: str(v) for k, v in sorted(data.items())}

def format_address(address: str) -> str:
    return address.lower().strip()

def validate_checksum(address: str) -> bool:
    if not address.startswith('0x') or len(address) != 42:
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[2:])

class CryptoUtils:
    @staticmethod
    def to_wei(amount: float, decimals: int = 18) -> int:
        return int(amount * (10 ** decimals))

    @staticmethod
    def from_wei(amount: int, decimals: int = 18) -> float:
        return amount / (10 ** decimals)