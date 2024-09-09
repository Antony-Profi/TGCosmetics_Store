import os
import asyncio
import logging

from dotenv import load_dotenv
from db.dbContext import createUserTableIfNotExsits
from app.bot import router
from aiogram import Bot, Dispatcher


load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ.get("TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    createUserTableIfNotExsits()

    await dp.start_polling(bot)

    await bot.delete_webhook(drop_pending_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
