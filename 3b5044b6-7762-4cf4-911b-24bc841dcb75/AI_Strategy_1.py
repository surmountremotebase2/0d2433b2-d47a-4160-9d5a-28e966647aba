from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the tickers of the assets you want to hold
        self.tickers = ["SPY", "QQQ", "AAPL", "GOOGL"]

    @property
    def assets(self):
        # The assets that this strategy will trade
        return self.tickers

    @property
    def interval(self):
        # The trading interval for this strategy. Since this is a buy-and-hold, 
        # the interval does not impact the trading decision. '1day' is a placeholder.
        return "1day"

    def run(self, data):
        # Create an equal-weight allocation for each asset in the portfolio
        allocation_dict = {ticker: 1 / len(self.tickers) for ticker in self.tickers}
        
        # Return the target allocation to maintain this portfolio indefinitely
        return TargetAllocation(allocation_dict)