from typing import Any, Dict, Optional

class ValidationError(Exception):
    pass

def validate_tx_payload(data: Any) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError('payload must be a dictionary')
    
    required_keys = {'tx_id', 'amount', 'currency', 'sender'}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - data.keys()
        raise ValidationError(f'missing required fields: {missing}')

    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValidationError('invalid amount: must be positive numeric')
        
    return data

def validate_address(address: str, chain: str) -> bool:
    if not isinstance(address, str) or len(address) < 26:
        return False
        
    if chain == 'btc' and not address.startswith(('1', '3', 'bc1')):
        return False
        
    if chain == 'eth' and not (address.startswith('0x') and len(address) == 42):
        return False
        
    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: str(v).strip() for k, v in data.items() if v is not None}