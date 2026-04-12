from aiogram import Bot, Dispatcher
import asyncio
from handlers import router
import os
from dotenv import load_dotenv
from database.models import async_main

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def main():
    await async_main()  
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')