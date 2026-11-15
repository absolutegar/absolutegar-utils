class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""

class DataValidationError(AbsolutegarError):
    """Raised when input data fails schema validation."""

class CryptoProviderError(AbsolutegarError):
    """Raised when external crypto API communication fails."""

class RateLimitExceededError(AbsolutegarError):
    """Raised when API rate limits are breached."""

class InsufficientFundsError(AbsolutegarError):
    """Raised when balance is inadequate for operations."""

class ConfigurationError(AbsolutegarError):
    """Raised when environment configuration is invalid."""