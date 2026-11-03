class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""


class ValidationError(AbsolutegarError):
    """Raised when input validation fails."""


class CryptoOperationError(AbsolutegarError):
    """Raised when cryptographic operations fail."""


class NetworkTimeoutError(AbsolutegarError):
    """Raised when a network request times out."""


class ConfigurationError(AbsolutegarError):
    """Raised when configuration is missing or invalid."""


class WalletAccessError(AbsolutegarError):
    """Raised when wallet interaction fails."""


def handle_exception(exc: Exception) -> None:
    """Minimal exception classification handler."""
    if isinstance(exc, (ValidationError, ConfigurationError)):
        print(f"Client error: {exc}")
    elif isinstance(exc, (CryptoOperationError, WalletAccessError)):
        print(f"Internal crypto error: {exc}")
    else:
        print(f"Unexpected system error: {exc}")