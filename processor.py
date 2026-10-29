import re
from typing import Any, Dict, List

ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
TX_HASH_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")


class InvalidTransactionError(Exception):
    pass


def validate_transaction(tx: Dict[str, Any]) -> None:
    if not isinstance(tx, dict):
        raise InvalidTransactionError("Transaction payload must be a dictionary")

    required_fields = {"sender", "recipient", "amount", "hash"}
    if not required_fields.issubset(tx.keys()):
        missing = required_fields - tx.keys()
        raise InvalidTransactionError(f"Missing required fields: {missing}")

    if not isinstance(tx["sender"], str) or not ADDRESS_REGEX.match(tx["sender"]):
        raise InvalidTransactionError("Invalid sender address format")

    if not isinstance(tx["recipient"], str) or not ADDRESS_REGEX.match(tx["recipient"]):
        raise InvalidTransactionError("Invalid recipient address format")

    if not isinstance(tx["hash"], str) or not TX_HASH_REGEX.match(tx["hash"]):
        raise InvalidTransactionError("Invalid transaction hash format")

    if not isinstance(tx["amount"], (int, float)) or tx["amount"] <= 0:
        raise InvalidTransactionError("Amount must be a positive number")


def process_transaction_queue(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for tx in transactions:
        try:
            validate_transaction(tx)
            tx_record = dict(tx)
            tx_record["status"] = "validated"
            processed.append(tx_record)
        except InvalidTransactionError as err:
            tx_record = dict(tx) if isinstance(tx, dict) else {"raw": tx}
            tx_record["status"] = "rejected"
            tx_record["error"] = str(err)
            processed.append(tx_record)
    return processed
