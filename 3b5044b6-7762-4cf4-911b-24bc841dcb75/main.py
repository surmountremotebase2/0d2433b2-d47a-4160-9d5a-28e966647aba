from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the asset we are interested in
        self.tickers = ["SPY"]
        # Initializing variables to store SMA values
        self.short_sma_period = 50  # Short-term SMA window
        self.long_sma_period = 200  # Long-term SMA window

    @property
    def assets(self):
        # List of assets this strategy will handle
        return self.tickers

    @property
    def interval(self):
        # Interval for data (daily for long-term strategies)
        return "1day"

    def run(self, data):
        # Allocates all or nothing to the SPY based on SMA crossover strategy
        allocation = 0  # Default to no allocation
        # Calculate the short and long SMAs for SPY
        short_sma = SMA("SPY", data["ohlcv"], self.short_sma_period)
        long_sma = SMA("SPY", data["ohlcv"], self.long_sma_period)
        
        if len(short_sma) > 0 and len(long_sma) > 0:
            current_price = data["ohlcv"][-1]["SPY"]["close"]
            # Check if the most recent short SMA is above the long SMA and price is above short SMA
            if short_sma[-1] > long_sma[-1] and current_price > short_sma[-1]:
                allocation = 1  # Allocate 100% to SPY
            log(f"Short SMA: {short_sba[-1]}, Long SMA: {long_sma[-1]}, Allocation: {allocation}")
        
        return TargetAllocation({"SPY": allocation})