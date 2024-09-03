from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="CLINIC"),
             KeyboardButton(text="SHOP")],
            [KeyboardButton(text="BAR"),
             KeyboardButton(text="КОНСУЛЬТАЦИЯ")],
            [KeyboardButton(text="СТАТУС ЗАКАЗА")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def create_clinic_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋About us"),
             KeyboardButton(text="Записаться")],
            [KeyboardButton(text="Контакты")],
            [KeyboardButton(text="🏠Главное меню")]
        ]
    )
    return keyboard
