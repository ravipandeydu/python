import random

# --- Base Classes ---


class TradingAccount:
    """Manages basic account functionalities like balance and trades."""

    def __init__(self, account_id: str, holder_name: str, initial_balance: float):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = initial_balance
        self.portfolio = {}  # e.g., {"AAPL": 10, "GOOGL": 5}
        print(f"TradingAccount for {self.holder_name} initialized.")

    def deposit(self, amount: float) -> bool:
        """Deposits funds into the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraws funds if the balance is sufficient."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def execute_trade(self, symbol: str, quantity: int, price: float, trade_type: str):
        """A generic method to be specialized by subclasses."""
        print(f"Executing generic trade for {symbol}...")
        # In a real system, this would update the portfolio and balance.


class RiskManagement:
    """Provides methods for assessing and managing trading risk."""

    def assess_portfolio_risk(self) -> str:
        """Assesses the overall risk of the current portfolio."""
        # Dummy implementation: risk is random for demonstration
        return random.choice(["Low", "Medium", "High"])

    def calculate_position_size(self, symbol: str, entry_price: float) -> float:
        """Calculates a safe position size based on risk parameters."""
        # Dummy implementation: returns a fixed size
        print(f"Calculating position size for {symbol} using RiskManagement logic.")
        return 1000.0 / entry_price  # Example: risk $1000 per trade


class AnalyticsEngine:
    """Provides market analysis tools."""

    def analyze_market_trend(self, symbol: str) -> dict:
        """Analyzes the market trend for a given symbol."""
        print(f"Analyzing market for {symbol} with AnalyticsEngine.")
        return {
            "trend": random.choice(["Bullish", "Bearish", "Neutral"]),
            "confidence": random.random(),
        }


class NotificationSystem:
    """Handles alerts and notifications for trading events."""

    def __init__(self, *args, **kwargs):
        # Using super() to handle multiple inheritance initialization
        super().__init__(*args, **kwargs)
        self._pending_notifications = []
        print("NotificationSystem initialized.")

    def set_price_alert(self, symbol: str, target_price: float, condition: str) -> bool:
        """Sets a price alert for a symbol."""
        alert = f"Alert set for {symbol}: price {condition} ${target_price}"
        self._pending_notifications.append(alert)
        print(alert)
        return True

    def get_pending_notifications(self) -> list:
        """Returns a list of pending notifications."""
        return self._pending_notifications


# --- Derived Classes ---


class StockTrader(TradingAccount, RiskManagement, AnalyticsEngine):
    """A trader specializing in stocks, combining account, risk, and analytics."""

    def __init__(self, account_id, holder_name, initial_balance):
        super().__init__(account_id, holder_name, initial_balance)
        print("StockTrader capabilities activated.")

    def execute_trade(self, symbol: str, quantity: int, price: float, trade_type: str):
        """Overrides base method for stock-specific trading logic."""
        print(f"Executing STOCK trade: {trade_type} {quantity} of {symbol} at ${price}")
        # Update portfolio logic would go here
        super().execute_trade(symbol, quantity, price, trade_type)


class CryptoTrader(TradingAccount, RiskManagement, NotificationSystem):
    """A trader specializing in crypto, combining account, risk, and notifications."""

    def __init__(self, account_id, holder_name, initial_balance):
        super().__init__(account_id, holder_name, initial_balance)
        print("CryptoTrader capabilities activated.")

    def execute_trade(self, symbol: str, quantity: int, price: float, trade_type: str):
        """Overrides base method for crypto-specific trading logic."""
        print(
            f"Executing CRYPTO trade: {trade_type} {quantity} of {symbol} at ${price}"
        )
        # Update portfolio logic would go here
        super().execute_trade(symbol, quantity, price, trade_type)


# --- Final Derived Class with Multiple Inheritance ---


class ProfessionalTrader(StockTrader, CryptoTrader):
    """
    A full-featured trader with all capabilities.
    Inherits from StockTrader and CryptoTrader, demonstrating MRO.
    The MRO will be: ProfessionalTrader -> StockTrader -> CryptoTrader -> TradingAccount ->
    RiskManagement -> AnalyticsEngine -> NotificationSystem -> object
    """

    def __init__(self, account_id, holder_name, initial_balance):
        # super() will follow the MRO to initialize all base classes correctly.
        super().__init__(account_id, holder_name, initial_balance)
        print("ProfessionalTrader fully activated with all capabilities.")

    def execute_diversified_strategy(self, strategy_params: dict) -> dict:
        """Executes a complex strategy involving both stocks and crypto."""
        print("\n--- Executing Diversified Strategy ---")
        stock_alloc = strategy_params["allocation"]["stocks"]
        crypto_alloc = strategy_params["allocation"]["crypto"]

        positions = []
        for stock in strategy_params["stocks"]:
            # Uses StockTrader's execute_trade via MRO
            self.execute_trade(stock, 10, 150.0, "BUY")
            positions.append({"symbol": stock, "type": "stock"})

        for crypto in strategy_params["crypto"]:
            # Uses CryptoTrader's execute_trade, but MRO finds StockTrader's first.
            # To call Crypto's specifically, one would need to be explicit.
            # However, for this demo, we'll let MRO rule.
            self.execute_trade(crypto, 5, 2500.0, "BUY")
            positions.append({"symbol": crypto, "type": "crypto"})

        # Use methods from all inherited classes
        risk = self.assess_portfolio_risk()
        self.set_price_alert("BTC", 50000, "above")

        return {"status": "executed", "positions": positions, "risk_assessment": risk}


# --- Verification using provided test cases ---

# Test Case 1: Multiple inheritance setup and MRO
print("--- Running Test Case 1 ---")
stock_trader = StockTrader("ST001", "John Doe", 50000.0)
crypto_trader = CryptoTrader("CT001", "Jane Smith", 25000.0)
pro_trader = ProfessionalTrader("PT001", "Mike Johnson", 100000.0)

# Check Method Resolution Order
mro_names = [cls.__name__ for cls in ProfessionalTrader.__mro__]
assert "ProfessionalTrader" in mro_names
assert "StockTrader" in mro_names
assert "CryptoTrader" in mro_names
print(f"MRO for ProfessionalTrader: {mro_names}")
print("✅ Test Case 1 Passed")

# Test Case 2: Account management capabilities
print("\n--- Running Test Case 2 ---")
assert stock_trader.account_id == "ST001"
assert stock_trader.balance == 50000.0
deposit_result = stock_trader.deposit(10000)
assert stock_trader.balance == 60000.0
assert deposit_result == True
withdrawal_result = stock_trader.withdraw(5000)
assert stock_trader.balance == 55000.0
print("✅ Test Case 2 Passed")

# Test Case 3: Risk management functionality
print("\n--- Running Test Case 3 ---")
risk_level = stock_trader.assess_portfolio_risk()
assert risk_level in ["Low", "Medium", "High"]
position_size = stock_trader.calculate_position_size("AAPL", 150.0)
assert isinstance(position_size, int) or isinstance(position_size, float)
assert position_size > 0
print("✅ Test Case 3 Passed")

# Test Case 4: Analytics capabilities
print("\n--- Running Test Case 4 ---")
market_data = stock_trader.analyze_market_trend("AAPL")
assert isinstance(market_data, dict)
assert "trend" in market_data
assert "confidence" in market_data
print("✅ Test Case 4 Passed")

# Test Case 5: Notification system for crypto trader
print("\n--- Running Test Case 5 ---")
alert_set = crypto_trader.set_price_alert("BTC", 45000, "above")
assert alert_set == True
notifications = crypto_trader.get_pending_notifications()
assert isinstance(notifications, list)
print("✅ Test Case 5 Passed")

# Test Case 6: Professional trader combining all features
print("\n--- Running Test Case 6 ---")
assert hasattr(pro_trader, "assess_portfolio_risk")  # From RiskManagement
assert hasattr(pro_trader, "analyze_market_trend")  # From AnalyticsEngine
assert hasattr(pro_trader, "set_price_alert")  # From NotificationSystem

# Execute complex trading strategy
strategy_result = pro_trader.execute_diversified_strategy(
    {
        "stocks": ["AAPL", "GOOGL"],
        "crypto": ["BTC", "ETH"],
        "allocation": {"stocks": 0.7, "crypto": 0.3},
    }
)
assert strategy_result["status"] == "executed"
assert len(strategy_result["positions"]) > 0
print("✅ Test Case 6 Passed")
