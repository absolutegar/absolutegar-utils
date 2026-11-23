class AbsoluteGarError(Exception):
    """Base exception for absolutegar-utils."""


class ConfigurationError(AbsoluteGarError):
    """Raised on invalid environment configuration."""


class ConnectionError(AbsoluteGarError):
    """Raised on crypto node connection failures."""


class ValidationError(AbsoluteGarError):
    """Raised on invalid payload data."""


class SigningError(AbsoluteGarError):
    """Raised during transaction signing process."""


class RateLimitError(AbsoluteGarError):
    """Raised when API rate limits exceeded."""


class TimeoutError(AbsoluteGarError):
    """Raised when network operations exceed limits."""