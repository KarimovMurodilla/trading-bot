"""This file represents a start logic."""

import asyncio
from sqlalchemy.exc import IntegrityError
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from src.db.database import Database
from src.language.translator import LocalizedTranslator
from src.bot.structures.keyboards import common
from src.utils.bybit_api import place_order, check_profit

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    """Start command handler."""
    await state.clear()

    await message.answer("Hi there! Choose pair", reply_markup=common.show_keyboard())


@start_router.message(F.text == "BTCUSDT")
async def start_handler(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    order_id, order_price = await place_order(message.text)
    await message.answer("Позиция открыта")
    task = asyncio.create_task(check_profit(message.text, order_price, order_id))

    result = await task
    if result:
        await message.answer(f"Позиция закрыта с прибылью: {result:.2f}%")
     

