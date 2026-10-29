import re
from typing import Dict, Optional


ADDRESS_PATTERNS: Dict[str, str] = {
    "ethereum": r"^0x[a-fA-F0-9]{40}$",
    "bitcoin_legacy": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "bitcoin_bech32": r"^bc1[a-zA-09-z1-9]{8,87}$",
    "solana": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
}

TX_HASH_PATTERNS: Dict[str, str] = {
    "ethereum": r"^0x[a-fA-F0-9]{64}$",
    "bitcoin": r"^[a-fA-F0-9]{64}$",
    "solana": r"^[1-9A-HJ-NP-Za-km-z]{87,88}$",
}


def validate_address(address: str, chain: str) -> bool:
    if not isinstance(address, str) or not address:
        return False
    chain_key = chain.lower()
    if chain_key == "bitcoin":
        return bool(
            re.match(ADDRESS_PATTERNS["bitcoin_legacy"], address)
            or re.match(ADDRESS_PATTERNS["bitcoin_bech32"], address.lower())
        )
    pattern = ADDRESS_PATTERNS.get(chain_key)
    if not pattern:
        raise ValueError(f"Unsupported network chain: {chain}")
    return bool(re.match(pattern, address))


def validate_tx_hash(tx_hash: str, chain: str) -> bool:
    if not isinstance(tx_hash, str) or not tx_hash:
        return False
    pattern = TX_HASH_PATTERNS.get(chain.lower())
    if not pattern:
        raise ValueError(f"Unsupported network chain: {chain}")
    return bool(re.match(pattern, tx_hash))


def sanitize_address(address: str, chain: str) -> Optional[str]:
    cleaned = address.strip()
    if validate_address(cleaned, chain):
        return cleaned.lower() if chain.lower() in ("ethereum", "bitcoin") else cleaned
    return None
