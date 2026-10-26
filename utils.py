import re
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List

HEX_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


class InvalidPayloadError(Exception):
    pass


def validate_transaction(tx: Dict[str, Any]) -> Dict[str, Any]:
    required_fields = {"sender", "receiver", "amount", "symbol"}
    if not required_fields.issubset(tx.keys()):
        missing = sorted(list(required_fields - tx.keys()))
        raise InvalidPayloadError(f"Missing required fields: {missing}")

    if not HEX_ADDRESS_PATTERN.match(str(tx["sender"] me if "sender" in tx else "")):
        raise InvalidPayloadError(f"Invalid sender address: {tx.get('sender')}")

    if not HEX_ADDRESS_PATTERN.match(str(tx.get("receiver", ""))):
        raise InvalidPayloadError(f"Invalid receiver address: {tx.get('receiver')}")

    try:
        amount = Decimal(str(tx["amount"]))
        if amount <= 0:
            raise InvalidPayloadError("Amount must be positive")
    except (InvalidOperation, TypeError):
        raise InvalidPayloadError(f"Invalid amount: {tx.get('amount')}")

    symbol = str(tx.get("symbol", "")).strip().upper()
    if not symbol.isalnum():
        raise InvalidPayloadError(f"Invalid asset symbol: {tx.get('symbol')}")

    return {
        "sender": str(tx["sender"]).lower(),
        "receiver": str(tx["receiver"]).lower(),
        "amount": amount,
        "symbol": symbol,
    }


def process_transaction_batch(
    batch: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    valid_records = []
    for raw_item in batch:
        if not isinstance(raw_item, dict):
            continue
        try:
            cleaned = validate_transaction(raw_item)
            valid_records.append(cleaned)
        except InvalidPayloadError:
            continue
    return valid_records
