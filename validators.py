from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_transaction_schema(data: Dict[str, Any]) -> None:
    required_fields = {'sender', 'recipient', 'amount', 'currency'}
    if not all(field in data for field in required_fields):
        raise ValidationError(f"Missing required fields: {required_fields - data.keys()}")
    
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValidationError("Invalid amount value")

def validate_network_payload(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False
    try:
        validate_transaction_schema(payload)
        return True
    except ValidationError:
        return False

def sanitize_input(data: str) -> str:
    return str(data).strip()[:256]