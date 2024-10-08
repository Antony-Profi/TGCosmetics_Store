from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from helper.replyKeyboardHelper import (
    getHomeReplyKeyboard as getHomeKeyboard,
    getClinicReplyKeyboard as getClinicButton,
    getShopReplyKeyboard as getShopButton,
    getBarReplyKeyboard as getBarButton,
    getOrderStatusReplyKeyboard as getOrderStatusButton
)
from database import getOrderStatus


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    keyboard = getHomeKeyboard()
    photo_path = "List_images/vodopad.jpeg"

    photo = FSInputFile(photo_path)

    await message.answer_photo(
        photo=photo,
        caption=
        f"Привет, <b>{message.from_user.full_name}💫</b>\n\n"
        f"Рады видеть в KRASOTA:\n"
        f"офлайн- и онлайн-магазин KRASOTA shop, клиника эстетической медицины KRASOTA clinic и особое пространство KRASOTA bar, в котором гедонизм сочетается с красотой.\n\n"
        f"Двигайтесь по меню ниже, чтобы узнать больше 💖",
        reply_markup=keyboard,
        parse_mode='HTML')


@router.message(F.text == "CLINIC")
async def sendingInfoClinicButtonWithAnImage(message: Message):
    keyboard = getClinicButton()
    try:
        await message.answer(
            "KRASOTA Clinic — место, где вы не только можете получить самые современные и эффективные услуги по уходу за кожей и волосами, "
            "но и всегда сможете почувствовать заботу самого высокого класса.\n\n"
            "Двигайтесь по меню ниже, чтобы узнать больше 💖",
            reply_markup=keyboard
        )

        photo_path = "List_images/vodopad.jpeg"

        photo = FSInputFile(photo_path)

        await message.answer_photo(photo=photo)

    except FileNotFoundError:
        await message.answer("Файл изображения не найден. Пожалуйста, проверьте путь к файлу.")
    except Exception as e:
        await message.answer("Произошла ошибка при отправке изображения.")
        print(f"Ошибка: {e}")


@router.message(F.text == "SHOP")
async def sendingDescriptionAndImageAndUpdatingBottomKeyboard(message: Message):
    keyboard = getShopButton()
    await message.answer(
        "KRASOTA shop – сервис заботы высочайшего класса.\n\n"
        
        "Место, где вы получите консультацию экспертов, помощь в индивидуальном подборе ухода"
        "и настоящее удовольствие от шопинга.\n\n"
        
        "Более 130 брендов и 5000 товаров в одном месте, и все это для вас.\n"
        "Двигайтесь по меню ниже, чтобы узнать больше 💖",
        reply_markup=keyboard
    )

    photo_path = "List_images/vodopad.jpeg"

    photo = FSInputFile(photo_path)

    await message.answer_photo(photo=photo)


@router.message(F.text == "🏠Главное меню")
async def backToMainMenuAndUpdatedKeyboard(message: Message):
    keyboard = getHomeKeyboard()

    await message.answer(
        "Главное меню",
        reply_markup=keyboard
    )


@router.message(F.text == "BAR")
async def sendingBarDescriptionsAndImagesAndTheCurrentKeyboard(message: Message):
    keyboard = getBarButton()

    await message.answer(
        "KRASOTA bar — живое и естественное продолжение концепта любви к себе, "
        "который создали и уже более 15 лет лелеют две сестры — Анна и Вера.\n"
        "Пространство гедонизма, свободы от стереотипов и предубеждения.\n\n"
        
        "Двигайтесь по меню ниже, чтобы узнать больше",
        reply_markup=keyboard
    )
    photo_path = "List_images/vodopad.jpeg"

    photo = FSInputFile(photo_path)

    await message.answer_photo(photo=photo)


@router.message(F.text == "Статус заказа")
async def command_status_order(message: Message):
    keyboard = getOrderStatusButton()

    await message.answer(
        "Выберите необходимый раздел 👇",
        reply_markup=keyboard
    )


@router.message(F.text == "🛍️За покупками")
async def commandForShoppingOnTheWebSite(message: Message):
    WebSite = "https://krasotashop.com/ru"
    await message.answer(
        f"Для перехода в ONLINE SHOP нажмите <a href='{WebSite}'>сюда</a>",
        parse_mode="HTML"
    )


@router.message(F.text == "📶Статус заказа")
async def ask_for_phone_number(message: Message):
    await message.answer(
        "Вы хотите отправить свой номер телефона этому боту?"
    )


@router.message(F.contact)
async def handle_phone_number(message: Message):
    user_phone_number = message.contact.phone_number

    order_info = getOrderStatus(user_phone_number)

    if order_info:
        response = (
            f"ID заказа: {order_info['id']}\n"
            f"Имя пользователя: {order_info['username']}\n"
            f"Название товара: {order_info['product_name']}\n"
            f"Количество : {order_info['quantity']}\n"
            f"Статус заказа: {order_info['status']}"
        )
        await message.answer(response)
    else:
        await message.answer("У вас нет активных заказов.")
