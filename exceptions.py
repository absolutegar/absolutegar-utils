class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""

class CryptoTransactionError(AbsolutegarError):
    """Raised when transaction execution fails."""

class InsufficientBalanceError(CryptoTransactionError):
    """Raised when wallet funds are insufficient."""

class InvalidSignatureError(CryptoTransactionError):
    """Raised during cryptographic verification failures."""

class NetworkTimeoutError(AbsolutegarError):
    """Raised on RPC or node communication timeouts."""

class RateLimitExceededError(AbsolutegarError):
    """Raised when API requests exceed threshold."""

class ConfigValidationError(AbsolutegarError):
    """Raised for malformed environment or config keys."""

def handle_crypto_exception(e: Exception) -> None:
    if isinstance(e, InsufficientBalanceError):
        raise ValueError("Action aborted: balance too low") from e
    if isinstance(e, NetworkTimeoutError):
        raise ConnectionError("Node connection unstable") from e
    raise e