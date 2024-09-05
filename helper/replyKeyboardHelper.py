from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def getHomeReplyKeyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="CLINIC"),
             KeyboardButton(text="SHOP")],
            [KeyboardButton(text="BAR"),
             KeyboardButton(text="Консультация")],
            [KeyboardButton(text="Статус заказа")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def getClinicReplyKeyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋About us"),
             KeyboardButton(text="📝Записаться")],
            [KeyboardButton(text="📱Контакты")],
            [KeyboardButton(text="🏠Главное меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def getShopReplyKeyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋About us"),
             KeyboardButton(text="🛻Доставка и оплата")],
            [KeyboardButton(text="📱Контакты"),
             KeyboardButton(text="🛒За покупками")],
            [KeyboardButton(text="🏠Главное меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def getBarReplyKeyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋About us"),
             KeyboardButton(text="📄Меню")],
            [KeyboardButton(text="📱Контакты")],
            [KeyboardButton(text="🏠Главное меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def getOrderStatusReplyKeyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📶Статус заказа", request_contact=True)],
            [KeyboardButton(text="🛍️За покупками")],
            [KeyboardButton(text="🏠Главное меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard
