class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""

class InsufficientLiquidityError(AbsolutegarError):
    """Raised when pool reserves are empty."""

class InvalidSignatureError(AbsolutegarError):
    """Raised when transaction signature is malformed."""

class NetworkTimeoutError(AbsolutegarError):
    """Raised when RPC node fails to respond."""

class ConfigurationError(AbsolutegarError):
    """Raised when environment variables are missing."""

def handle_critical_failure(error: Exception) -> None:
    if not isinstance(error, AbsolutegarError):
        raise RuntimeError("Unhandled non-crypto exception caught") from error
    print(f"Critical failure in absolutegar: {type(error).__name__}")