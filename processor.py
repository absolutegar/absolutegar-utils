import re
from typing import Any, Dict, List, Optional


class ValidationError(Exception):
    pass


def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def validate_payload(payload: Dict[str, Any]) -> None:
    required_keys = {"sender", "recipient", "amount", "asset"}
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary")
    missing = required_keys - payload.keys()
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")
    if not validate_address(payload["sender"]):
        raise ValidationError(f"Invalid sender address: {payload['sender']}")
    if not validate_address(payload["recipient"]):
        raise ValidationError(f"Invalid recipient address: {payload['recipient']}")
    if not isinstance(payload["amount"], (int, float)) or payload["amount"] <= 0:
        raise ValidationError("Amount must be a positive number")
    if not isinstance(payload["asset"], str) or not payload["asset"].isalnum():
        raise ValidationError("Asset must be an alphanumeric string")


class TransactionProcessor:
    def __init__(self, supported_assets: Optional[List[str]] = None) -> None:
        self.supported_assets = supported_assets or ["BTC", "ETH", "USDT"]

    def process_batch(self, raw_transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for raw_tx in raw_transactions:
            try:
                validate_payload(raw_tx)
                if raw_tx["asset"] not in self.supported_assets:
                    raise ValidationError(f"Unsupported asset: {raw_tx['asset']}")
                processed.append({
                    "sender": raw_tx["sender"],
                    "recipient": raw_tx["recipient"],
                    "amount": float(raw_tx["amount"]),
                    "asset": raw_tx["asset"].upper(),
                    "status": "validated"
                })
            except ValidationError as err:
                processed.append({
                    "tx": raw_tx,
                    "status": "failed",
                    "error": str(err)
                })
        return processed
