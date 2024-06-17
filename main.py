import asyncio
from start import start_router
import logging
from config import set_my_menu, dp, bot


async def main():
    await set_my_menu()# запуск бота
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')