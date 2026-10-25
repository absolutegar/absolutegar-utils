import logging

class ValidationError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise ValidationError("Invalid input type: expected dict")
    if "address" not in data or len(data["address"]) != 42:
        raise ValidationError("Invalid wallet address format")
    if not isinstance(data.get("amount"), (int, float)) or data["amount"] <= 0:
        raise ValidationError("Invalid transaction amount")
    return True

def process_transactions(queue):
    logger = logging.getLogger(__name__)
    while True:
        try:
            item = queue.get(timeout=1)
            if validate_input(item):
                logger.info(f"Processing: {item['address']}")
        except ValidationError as e:
            logger.error(f"Validation failure: {e}")
        except Exception as e:
            logger.debug(f"Queue processing interruption: {e}")
            break