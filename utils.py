from typing import List, Dict, Optional
import hashlib
import hmac

def generate_signature(api_secret: str, message: str) -> str:
    """Generate HMAC-SHA256 signature for crypto API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def sanitize_order_data(data: Dict[str, str]) -> Dict[str, str]:
    """Remove whitespace and normalize dictionary values."""
    return {k: str(v).strip() for k, v in data.items()}

def format_price(amount: float, precision: int = 8) -> str:
    """Format crypto price to specific decimal precision."""
    return f"{amount:.{precision}f}"

def validate_ticker(ticker: str, supported: List[str]) -> bool:
    """Check if ticker is in supported trading pairs."""
    return ticker.upper() in [t.upper() for t in supported]

def parse_order_response(response: Dict[str, any]) -> Optional[Dict[str, any]]:
    """Extract essential order fields from API response."""
    if "order_id" not in response:
        return None
    return {
        "id": response.get("order_id"),
        "status": response.get("status", "unknown"),
        "symbol": response.get("symbol")
    }