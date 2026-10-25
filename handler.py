import hashlib
import hmac
import time
from typing import Dict, Optional


class CryptoHandler:
    """Handler for signing and verifying cryptographic API requests."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        """Initialize the handler with API credentials.

        Args:
            api_key: Public API identifier.
            api_secret: Secret key used for HMAC signing.
        """
        self.api_key = api_key
        self.api_secret = api_secret.encode("utf-8")

    def generate_signature(self, payload: str, timestamp: int) -> str:
        """Generate HMAC SHA256 signature for API authentication.

        Args:
            payload: Stringified request payload.
            timestamp: Unix timestamp in milliseconds.

        Returns:
            Hexadecimal HMAC signature string.
        """
        message = f"{timestamp}{payload}".encode("utf-8")
        return hmac.new(self.api_secret, message, hashlib.sha256).hexdigest()

    def verify_signature(self, payload: str, timestamp: int, signature: str) -> bool:
        """Verify an incoming payload signature against expected digest.

        Args:
            payload: Stringified payload received.
            timestamp: Unix timestamp in milliseconds.
            signature: Hexadecimal signature string to verify.

        Returns:
            True if signature matches, False otherwise.
        """
        expected = self.generate_signature(payload, timestamp)
        return hmac.compare_digest(expected, signature)

    def build_headers(self, payload: str, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Build HTTP authentication headers for API requests.

        Args:
            payload: Stringified payload to sign.
            extra: Optional additional headers to merge.

        Returns:
            Dictionary containing complete request headers.
        """
        timestamp = int(time.time() * 1000)
        sig = self.generate_signature(payload, timestamp)
        headers = {
            "X-API-KEY": self.api_key,
            "X-API-SIGNATURE": sig,
            "X-API-TIMESTAMP": str(timestamp),
            "Content-Type": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers
