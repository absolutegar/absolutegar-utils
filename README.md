[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# absolutegar-utils

`absolutegar-utils` is a high-performance Python toolkit engineered for low-latency cryptocurrency algorithmic trading, Web3 payload construction, and exchange data normalization. Built for quantitative traders and MEV searchers, it streamlines cross-venue market data ingestion and EVM transaction assembly.

## Features

- **Cross-Venue Book Normalizer:** Ingests raw WebSocket order book snapshots from CEXs (Binance, Bybit) and DEXs (Uniswap V3, Curve) into structured NumPy arrays.
- **Optimized ABI Encoder:** Provides fast EVM payload construction and method selector computation with lower overhead than standard Web3 bindings.
- **Dynamic Fee Estimator:** Calculates optimal EIP-1559 base and priority fees using real-time block telemetry and sliding-window percentiles.
- **EIP-712 Signature Tools:** Simplifies signing, hashing, and validating typed structured data for decentralized exchange orders.

## Installation

Install the latest release via `pip`:

```bash
pip install absolutegar-utils
```

Or build directly from the source repository:

```bash
git clone https://github.com/Developer/absolutegar-utils.git
cd absolutegar-utils
pip install .
```

## Basic Usage

The following example demonstrates how to estimate optimal EIP-1559 gas fees and parse a normalized order book snapshot:

```python
from absolutegar_utils import FeeEstimator, OrderBookParser

# Calculate priority and max fees for EVM transactions
estimator = FeeEstimator(rpc_url="https://eth-mainnet.g.alchemy.com/v2/demo")
suggested_fees = estimator.get_optimal_fees(target_percentile=75)

print(f"Base Fee: {suggested_fees.base_fee_gwei:.2f} Gwei")
print(f"Priority Fee: {suggested_fees.priority_fee_gwei:.2f} Gwei")

# Normalize raw exchange payload
raw_data = {
    "bids": [["65000.50", "1.2"], ["64999.00", "0.5"]],
    "asks": [["65001.00", "0.8"], ["65002.