class CryptoBaseError(Exception):
    """Base exception for absolutegar-utils."""


class DataFormatError(CryptoBaseError):
    """Raised when input data fails schema validation."""


class ExchangeConnectionError(CryptoBaseError):
    """Raised when connectivity to exchange is lost."""


class RateLimitError(CryptoBaseError):
    """Raised when API rate limit is exceeded."""


class InsufficientFundsError(CryptoBaseError):
    """Raised when wallet balance is too low."""


def validate_response(data: dict) -> None:
    if not isinstance(data, dict):
        raise DataFormatError("Invalid response format")
    if "error" in data:
        raise CryptoBaseError(f"API Error: {data['error']}")


def handle_request_error(status_code: int) -> None:
    if status_code == 429:
        raise RateLimitError("Rate limit reached")
    if status_code >= 500:
        raise ExchangeConnectionError("Remote exchange server error")