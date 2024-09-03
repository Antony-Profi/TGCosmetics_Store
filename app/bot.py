from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from InlineKeyboardHelper.menu import create_menu, create_clinic_menu


router = Router()


@router.message(CommandStart())
async def gettingTheUsersFullName(message: Message):
    keyboard = create_menu()
    photo_path = "C:/Users/User/Desktop/tgMarketPlace/vodopad.jpeg"

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
async def show_image_and_description(message: Message):
    keyboard = create_clinic_menu()
    try:
        await message.answer(
            "KRASOTA Clinic — место, где вы не только можете получить самые современные и эффективные услуги по уходу за кожей и волосами, "
            "но и всегда сможете почувствовать заботу самого высокого класса.\n\n"
            "Двигайтесь по меню ниже, чтобы узнать больше 💖",
            reply_markup=keyboard
        )

        photo_path = "C:/Users/User/Desktop/tgMarketPlace/vodopad.jpeg"

        photo = FSInputFile(photo_path)

        await message.answer_photo(photo=photo)

    except FileNotFoundError:
        await message.answer("Файл изображения не найден. Пожалуйста, проверьте путь к файлу.")
    except Exception as e:
        await message.answer("Произошла ошибка при отправке изображения.")
        print(f"Ошибка: {e}")


@router.message(F.text == "SHOP")
async def shop(message: Message):
    await message.answer(
        "KRASOTA shop – сервис заботы высочайшего класса.\n\n"
        
        "Место, где вы получите консультацию экспертов, помощь в индивидуальном подборе ухода"
        "и настоящее удовольствие от шопинга.\n\n"
        
        "Более 130 брендов и 5000 товаров в одном месте, и все это для вас.\n"
        "Двигайтесь по меню ниже, чтобы узнать больше 💖"
    )

    photo_path = "C:/Users/User/Desktop/tgMarketPlace/vodopad.jpeg"

    photo = FSInputFile(photo_path)

    await message.answer_photo(photo=photo)


@router.message(F.text == "🏠Главное меню")
async def back_to_main_menu(message: Message):
    keyboard = create_menu()

    await message.answer(
        "Главное меню",
        reply_markup=keyboard
    )
