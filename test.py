from pybit.unified_trading import HTTP

from src.configuration import conf

session = HTTP(
    testnet=False,
    api_key='conf.BYBIT_API_KEY',
    api_secret='conf.BYBIT_API_SECRET',
)

PAIR = 'ETHUSDT'

def get_price():
    ticker = session.get_tickers(category="linear", symbol=PAIR)
    return float(ticker['result']['list'][0]['lastPrice'])

res = get_price()
print(res)
