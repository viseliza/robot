from .config import TOKEN_BOT

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot, storage=MemoryStorage())