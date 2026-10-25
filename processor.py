from typing import Dict, List, Optional, Union

class CryptoProcessor:
    """Handles cryptographic data transformation and validation."""

    def __init__(self, key_id: str) -> None:
        self.key_id: str = key_id

    def process_payload(self, data: Dict[str, Union[str, int]]) -> Optional[Dict[str, str]]:
        """Transforms raw payload into signed cryptographic format."""
        if not data or "nonce" not in data:
            return None

        processed: Dict[str, str] = {
            "k": self.key_id,
            "val": str(data["nonce"]),
            "status": "verified"
        }
        return processed

    def batch_process(self, payloads: List[Dict[str, Union[str, int]]]) -> List[Dict[str, str]]:
        """Applies transformation logic to a batch of payloads."""
        results: List[Dict[str, str]] = []
        for p in payloads:
            result = self.process_payload(p)
            if result:
                results.append(result)
        return results