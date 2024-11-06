from pybit.unified_trading import HTTP

from src.configuration import conf

session = HTTP(
    testnet=False,
    api_key=conf.BYBIT_API_KEY,
    api_secret=conf.BYBIT_API_SECRET,
)


async def get_price(pair: str):
    ticker = session.get_tickers(category="linear", symbol=pair)
    return float(ticker['result']['list'][0]['lastPrice'])

async def place_order(pair: str):
    order = session.place_order(
        category="linear",
        symbol=pair,
        side="Buy",
        orderType="Market",
        qty=0.01
    )
    return order['result']['orderId'], float(order['result']['price'])

async def close_order(pair, order_id):
    session.cancel_order(category="linear", symbol=pair, orderId=order_id)

async def check_profit(pair, order_price, order_id):
    while True:
        current_price = await get_price(pair)
        profit_percentage = (current_price - order_price) / order_price * 100

        if profit_percentage >= 0.1:
            await close_order(pair, order_id)
            return profit_percentage

        await asyncio.sleep(10)
