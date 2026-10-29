from typing import Any

class ValidationError(Exception):
    """Base exception for validation failures."""

def validate_transaction_data(data: dict) -> None:
    required_fields = {"address", "amount", "asset"}
    if not isinstance(data, dict):
        raise ValidationError("Invalid payload format")
    
    if not required_fields.issubset(data.keys()):
        missing = required_fields - data.keys()
        raise ValidationError(f"Missing fields: {missing}")

    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        raise ValidationError("Invalid amount value")

def validate_network_id(network_id: Any) -> None:
    if not isinstance(network_id, str) or len(network_id) < 3:
        raise ValidationError("Invalid network identifier")