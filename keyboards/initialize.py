from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

class Keyboard:
    def main():
        keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        
        keyboard.add(
            KeyboardButton('🛴 Test'), 
            KeyboardButton('👤 Профиль')
        )

        return keyboard