from aiogram import executor
from database import create_db
from commands import dp
import os 
import logging
from config.config import DEBUG

# Создание папки логирования, если нету
if not os.path.exists('./logs'):
    os.mkdir('./logs')

# Установка уровня логирования
"""
    Вариант логирования в один файл с перезаписью файла под 0 после перезапуска

    Либо без перезаписи под 0, с дозаписью, при filemode='a'
"""
logging.basicConfig(filename=f"./logs/latest.log", encoding='utf-8', filemode='w', level=logging.DEBUG if DEBUG else logging.ERROR)

"""
    Вариант логирования в разные файлы при запуске
"""
"""
from time import time

logging.basicConfig(filename=f"./logs/{time()}.log", encoding='utf-8', level=logging.DEBUG if DEBUG else logging.ERROR)
"""

async def on_startup(dispatcher):
    create_db()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
