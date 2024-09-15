import asyncio
import logging

from dotenv import load_dotenv
from db.dbContext import getConnection, createUserTableIfNotExists
from pro.bot import router
from aiogram import Bot, Dispatcher
from app import app
from multiprocessing import Process
from os import environ


load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=environ.get("TOKEN"))
dp = Dispatcher()


async def startBot():
    dp.include_router(router)
    conn = getConnection()
    cur = conn.cursor()
    createUserTableIfNotExists(conn, cur)
    conn.close()

    await dp.start_polling(bot)


def startWebSite():
    app.run(host="0.0.0.0", port=int(environ.get("WEB-SITE_PORT")))


def main():
    web_process = Process(target=startWebSite)
    web_process.start()

    asyncio.run(startBot())

    web_process.join()


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"An error occurred: {e}")
        app.logger.error(f"An error occurred: {e}")
