import logging
from typing import Any, Optional

class ProcessingError(Exception):
    pass

def validate_payload(data: Any) -> bool:
    if not isinstance(data, dict):
        raise ProcessingError('invalid data structure')
    if 'nonce' not in data:
        raise ProcessingError('missing required nonce field')
    return True

def process_transaction(payload: Any) -> Optional[dict]:
    try:
        validate_payload(payload)
        return {'status': 'success', 'id': payload.get('nonce')}
    except ProcessingError as e:
        logging.error(f'validation failure: {e}')
        return None
    except Exception as e:
        logging.critical(f'unexpected system fault: {e}')
        return None

def batch_process(items: list) -> list:
    results = []
    for item in items:
        result = process_transaction(item)
        if result:
            results.append(result)
    return results