class CryptoUtilsError(Exception):
    """Base exception for all crypto utility errors."""


class InvalidAddressError(CryptoUtilsError):
    def __init__(self, address: str, chain: str = "unknown") -> None:
        self.address = address
        self.chain = chain
        super().__init__(f"Invalid {chain} address format: '{address}'")


class InsufficientBalanceError(CryptoUtilsError):
    def __init__(self, required: float, available: float, symbol: str) -> None:
        self.required = required
        self.available = available
        self.symbol = symbol
        super().__init__(
            f"Insufficient {symbol} balance: required {required}, available {available}"
        )


class SignatureVerificationError(CryptoUtilsError):
    def __init__(self, message: str = "Signature verification failed") -> None:
        super().__init__(message)


class RateLimitExceededError(CryptoUtilsError):
    def __init__(self, provider: str, retry_after: int | None = None) -> None:
        self.provider = provider
        self.retry_after = retry_after
        msg = f"Rate limit exceeded for provider '{provider}'"
        if retry_after is not None:
            msg += f". Retry after {retry_after} seconds"
        super().__init__(msg)


class StalePriceError(CryptoUtilsError):
    def __init__(self, symbol: str, age_seconds: float, max_age: float) -> None:
        self.symbol = symbol
        self.age_seconds = age_seconds
        self.max_age = max_age
        super().__init__(
            f"Price feed for {symbol} is stale ({age_seconds:.1f}s old, max allowed {max_age}s)"
        )
