# absolutegar-utils

A robust Python toolkit designed for automated cryptocurrency market analysis and portfolio monitoring. It provides efficient abstractions for interacting with exchange APIs and processing high-frequency price data.

## Features

*   **Unified API Adapters:** Normalized wrappers for Binance and CCXT-based exchanges to simplify trade execution and historical data retrieval.
*   **Volatility Analysis:** Built-in modules to calculate real-time Bollinger Bands, RSI, and custom momentum indicators using `pandas` and `numpy`.
*   **Async Portfolio Tracking:** Asynchronous asset monitoring capable of streaming balance updates across multiple wallets without blocking the main event loop.
*   **Alerting Engine:** Integrated hooks for Telegram and Discord notifications to trigger instant alerts on customizable price thresholds.

## Installation

Ensure you have Python 3.9+ installed. Install the package via pip:

```bash
pip install absolutegar-utils
```

To enable advanced charting dependencies, use the optional install:

```bash
pip install absolutegar-utils[charts]
```

## Basic Usage

Initialize the client to fetch market data and monitor a trading pair asynchronously:

```python
import asyncio
from absolutegar import MarketClient

async def main():
    client = MarketClient(exchange='binance')
    
    # Fetch real-time ticker
    ticker = await client.get_ticker('BTC/USDT')
    print(f"Current Price: {ticker['last']}")

    # Setup a price alert
    await client.monitor_price('BTC/USDT', target=65000, callback=lambda: print("Target reached!"))

if __name__ == "__main__":
    asyncio.run(main())
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.