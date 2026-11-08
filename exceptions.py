class AbsoluteGarError(Exception):
    """Base exception for absolutegar-utils."""


class InsufficientBalanceError(AbsoluteGarError):
    """Raised when wallet balance is below threshold."""


class ChainConnectionError(AbsoluteGarError):
    """Raised on RPC provider connection failure."""


class InvalidSignatureError(AbsoluteGarError):
    """Raised when cryptographic signature verification fails."""


class RateLimitError(AbsoluteGarError):
    """Raised when API requests exceed limits."""


def handle_crypto_error(err: Exception) -> None:
    """Centralized error classification for crypto ops."""
    if isinstance(err, (ConnectionError, TimeoutError)):
        raise ChainConnectionError("Network connectivity issue detected") from err
    if isinstance(err, ValueError) and "signature" in str(err).lower():
        raise InvalidSignatureError("Invalid cryptographic signature provided") from err
    if isinstance(err, (AttributeError, KeyError)):
        raise AbsoluteGarError("Malformed response from provider") from err
    raise err