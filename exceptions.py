class AbsolutegarError(Exception):
    """Base exception for absolutegar-utils."""

class DataProcessingError(AbsolutegarError):
    """Raised when data operations fail."""

class ValidationError(AbsolutegarError):
    """Raised when input validation fails."""

class OptimizationError(AbsolutegarError):
    """Raised when performance tuning fails."""

class RateLimitError(AbsolutegarError):
    """Raised when throughput limits are exceeded."""

class MemoryExceededError(AbsolutegarError):
    """Raised when memory constraints are breached."""

__all__ = [
    'AbsolutegarError',
    'DataProcessingError',
    'ValidationError',
    'OptimizationError',
    'RateLimitError',
    'MemoryExceededError'
]