from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Показать изображение и описание")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

