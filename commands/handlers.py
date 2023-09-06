from config import dp, bot
from config.config import DEBUG
from database import User, Group
from keyboards import Keyboard

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import logging

# Включение логгера на уровне информации
#logging.setLevel()

class Options(StatesGroup):
    enter_group = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    try:
        # Получаем пользователя
        user_id = message.chat.id
        
        # Дебаг при логгере
        #logging.

        # Проверяем находится ли он в базе
        if not await User.get(user_id):
            # Добавляем пользователя
            await User.add(user_id)

        await bot.send_message(chat_id=user_id, text="👋 Добро пожаловать", reply_markup=Keyboard.main())
    except Exception as error:
        print(f'[ Commands/Handlers/process_start_command ] Error: {error}')

