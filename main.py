import asyncio

import logging

from aiogram import Dispatcher, Bot

from handlers.handlers import router
from config import TELEGRAM_TOKEN

dp = Dispatcher()
bot = Bot(TELEGRAM_TOKEN)

async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
