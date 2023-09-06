from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

class Keyboard:
    def main():
        keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        
        keyboard.add(*[
            '👨‍🎓 Выбор группы',
            '👀 Просмотр замен'
        ])

        return keyboard