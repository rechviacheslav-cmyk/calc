from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from router import router
import logging
import asyncio
from web import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())