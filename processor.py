from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Union


class CryptoProcessingError(Exception):
    pass


class InvalidTransactionError(CryptoProcessingError):
    pass


class ValueOverflowError(CryptoProcessingError):
    pass


class TransactionProcessor:
    MAX_WEI = Decimal("115792089237316195423570985008687907853269984665640564039457584007913129639935")

    def parse_wei_amount(self, raw_value: Union[str, int, float, Decimal]) -> Decimal:
        try:
            val = Decimal(str(raw_value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise InvalidTransactionError(f"Cannot parse value '{raw_value}' into Decimal") from exc

        if val < 0:
            raise InvalidTransactionError(f"Transaction amount cannot be negative: {val}")

        if val > self.MAX_WEI:
            raise ValueOverflowError(f"Value {val} exceeds 256-bit unsigned integer maximum")

        if val.as_tuple().exponent < 0:
            raise InvalidTransactionError(f"Fractional Wei values are not allowed: {val}")

        return val

    def decode_hex_data(self, hex_str: str) -> bytes:
        if not isinstance(hex_str, str):
            raise InvalidTransactionError("Hex payload must be a string")

        clean_str = hex_str[2:] if hex_str.startswith("0x") else hex_str
        if len(clean_str) % 2 != 0:
            clean_str = "0" + clean_str

        try:
            return bytes.fromhex(clean_str)
        except ValueError as exc:
            raise InvalidTransactionError(f"Malformed hex string: {hex_str}") from exc

    def process_transaction(self, tx_payload: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(tx_payload, dict):
            raise InvalidTransactionError("Payload must be a dictionary")

        required_fields = ("to", "value", "data")
        for field in required_fields:
            if field not in tx_payload:
                raise InvalidTransactionError(f"Missing required field: '{field}'")

        parsed_value = self.parse_wei_amount(tx_payload["value"])
        decoded_data = self.decode_hex_data(tx_payload.get("data", ""))

        return {
            "to": str(tx_payload["to"]).lower(),
            "value_wei": int(parsed_value),
            "data_bytes": decoded_data,
            "is_contract_call": len(decoded_data) > 0,
        }
