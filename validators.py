import re
from typing import Optional

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

class CryptoValidator:
    @staticmethod
    def is_valid_address(address: str) -> bool:
        return bool(ADDRESS_PATTERN.match(address))

    @staticmethod
    def sanitize_symbol(symbol: str) -> str:
        return re.sub(r'[^A-Z0-9]', '', symbol.upper())

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount >= 0

    @classmethod
    def validate_tx_payload(cls, data: dict) -> bool:
        required = ['from', 'to', 'amount']
        if not all(k in data for k in required):
            return False
        return (
            cls.is_valid_address(data['from'])
            and cls.is_valid_address(data['to'])
            and cls.validate_amount(data['amount'])
        )