from aiogram import Router, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from InlineKeyboardHelper.menu import create_menu


router = Router()


@router.message(CommandStart())
async def gettingTheUsersFullName(message: Message):
    keyboard = create_menu()
    await message.answer(
        f"Привет, <b>{message.from_user.full_name}💫</b>\n\n"
        f"Рады видеть в KRASOTA:\n"
        f"офлайн- и онлайн-магазин KRASOTA shop, клиника эстетической медицины KRASOTA clinic и особое пространство KRASOTA bar, в котором гедонизм сочетается с красотой.\n\n"
        f"Двигайтесь по меню ниже, чтобы узнать больше 💖",
        reply_markup=keyboard,
        parse_mode='HTML')


@router.message(F.text == "Показать изображение и описание")
async def show_image_and_description(message: Message):
    await message.answer_photo(
        photo="C:/Users/User/Desktop/tgMarketPlace/водопад.jpeg",
        caption="KRASOTA Clinic — место, где вы не только можете получить самые современные и эффективные услуги по уходу за кожей и волосами, но и всегда сможете почувствовать заботу самого высокого класса.\n\n"
                "Двигайтесь по меню ниже, чтобы узнать больше 💖"
    )
