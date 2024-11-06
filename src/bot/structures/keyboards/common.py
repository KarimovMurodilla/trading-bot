from aiogram import types


def show_keyboard():
    kb = [
        [types.KeyboardButton(text="BTCUSDT")],
        [types.KeyboardButton(text="ETHUSDT")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard
