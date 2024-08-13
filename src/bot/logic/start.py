"""This file represents a start logic."""

from sqlalchemy.exc import IntegrityError
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from src.bot.filters.register_filter import RegisterFilter
from src.db.database import Database
from src.language.translator import LocalizedTranslator

start_router = Router(name='start')


@start_router.message(CommandStart(), RegisterFilter())
async def start_handler(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    """Start command handler."""
    await state.clear()

    await message.answer("Hi there!")