# absolutegar-utils

A collection of high-performance Python utilities designed for cryptocurrency market data analysis and automated execution. This library streamlines integration with exchange APIs while providing robust tools for local data processing and technical signal generation.

## Features

*   **Async Exchange Adapters:** Unified asynchronous wrappers for major crypto exchanges, supporting REST and WebSocket streams with automatic rate-limit handling.
*   **Vectorized Technical Indicators:** Optimized calculation of common trading indicators (RSI, Bollinger Bands, MACD) leveraging `pandas` and `numpy` for speed.
*   **Portfolio Reconciliation:** Automated utilities to track multi-exchange balances and calculate unrealized PnL in real-time.
*   **Signed Request Signing:** Secure, production-ready HMAC-SHA256 signature generators for private API endpoint authentication.

## Installation

Install the latest version directly via pip:

```bash
pip install absolutegar-utils
```

For local development and testing:

```bash
git clone https://github.com/developer/absolutegar-utils.git
cd absolutegar-utils
pip install -r requirements.txt
```

## Basic Usage

The following example demonstrates how to initialize a secure client and fetch the latest ticker price for a trading pair:

```python
from absolutegar_utils.client import ExchangeClient

# Initialize client with environment variables
client = ExchangeClient(api_key='YOUR_KEY', api_secret='YOUR_SECRET')

# Fetch real-time ticker data
ticker = client.get_ticker("BTC/USDT")

print(f"Current Price: {ticker['last_price']}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.