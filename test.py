from pybit.unified_trading import HTTP

from src.configuration import conf

session = HTTP(
    # testnet=False,
    api_key=conf.BYBIT_API_KEY,
    api_secret=conf.BYBIT_API_SECRET,
)

session.get_orderbook(category="linear", symbol="BTCUSDT")

