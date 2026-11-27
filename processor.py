import re
from typing import Any, Dict, List


class InvalidTransactionError(Exception):
    pass


class TransactionProcessor:
    HEX_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
    SUPPORTED_ASSETS = {"BTC", "ETH", "USDT", "SOL"}

    def __init__(self, default_asset: str = "ETH") -> None:
        self.default_asset = default_asset

    def validate_payload(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(tx, dict):
            raise InvalidTransactionError("Transaction payload must be a dictionary")

        recipient = tx.get("recipient")
        if not recipient or not isinstance(recipient, str):
            raise InvalidTransactionError("Missing or invalid recipient address")

        if not self.HEX_ADDRESS_REGEX.match(recipient):
            raise InvalidTransactionError(f"Invalid EVM address format: {recipient}")

        amount = tx.get("amount")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidTransactionError("Amount must be a positive number")

        asset = str(tx.get("asset", self.default_asset)).upper()
        if asset not in self.SUPPORTED_ASSETS:
            raise InvalidTransactionError(f"Unsupported crypto asset: {asset}")

        return {
            "recipient": recipient,
            "amount": float(amount),
            "asset": asset,
            "nonce": int(tx.get("nonce", 0)),
        }

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed_transactions: List[Dict[str, Any]] = []
        for item in batch:
            try:
                validated_tx = self.validate_payload(item)
                validated_tx["status"] = "validated"
                processed_transactions.append(validated_tx)
            except InvalidTransactionError as err:
                processed_transactions.append(
                    {"raw": item, "status": "rejected", "error": str(err)}
                )
        return processed_transactions
