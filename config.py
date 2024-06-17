from aiogram import Bot, Dispatcher, types

BOT_TOKEN = '7155093565:AAHlqxjFKuF7-a9naGBHHbVuJcKb634QA2A'

dp = Dispatcher()
bot = Bot(BOT_TOKEN)


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало")
    ])