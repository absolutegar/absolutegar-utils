import re
from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def is_valid_eth_address(address: str) -> bool:
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    return bool(re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash))


def validate_transaction_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    required_keys = {"sender", "recipient", "amount", "tx_hash"}
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - set(payload.keys())
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    sender = str(payload["sender"])
    recipient = str(payload["recipient"])
    tx_hash = str(payload["tx_hash"])
    amount = payload["amount"]

    if not is_valid_eth_address(sender):
        raise ValidationError(f"Invalid sender address: {sender}")

    if not is_valid_eth_address(recipient):
        raise ValidationError(f"Invalid recipient address: {recipient}")

    if not is_valid_tx_hash(tx_hash):
        raise ValidationError(f"Invalid transaction hash: {tx_hash}")

    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValidationError(f"Invalid transaction amount: {amount}")

    return {
        "sender": sender.lower(),
        "recipient": recipient.lower(),
        "amount": float(amount),
        "tx_hash": tx_hash.lower(),
    }


def process_batch_payloads(raw_payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    validated_records = []
    for item in raw_payloads:
        try:
            clean_item = validate_transaction_payload(item)
            validated_records.append(clean_item)
        except ValidationError:
            continue
    return validated_records
