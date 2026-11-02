class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""


class ChainConnectionError(AbsolutegarError):
    """Raised when blockchain node is unreachable."""


class WalletBalanceError(AbsolutegarError):
    """Raised during insufficient fund scenarios."""


class TransactionValidationError(AbsolutegarError):
    """Raised for malformed crypto transactions."""


def handle_crypto_error(err: Exception) -> None:
    if isinstance(err, (ChainConnectionError, WalletBalanceError, TransactionValidationError)):
        print(f"[CRYPTO ERROR]: {err.__class__.__name__} - {err}")
    else:
        print(f"[FATAL ERROR]: Unexpected system exception: {err}")


def validate_tx_amount(amount: float) -> None:
    if amount <= 0:
        raise TransactionValidationError("Transaction amount must be positive")


def validate_node_status(status: bool) -> None:
    if not status:
        raise ChainConnectionError("RPC node node rejected connection request")