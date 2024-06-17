from aiogram import Router, F, types
from aiogram.filters import Command

from parser import CarCrawler

start_router = Router()


@start_router.callback_query(lambda c: c.data == 'send_info')
async def send_lk(callback: types.CallbackQuery):
    await callback.answer()
    await callback.answer("Начинаю сбор данных...")
    crawler = CarCrawler()
    car_data = await crawler.get_cars()
    for car in car_data:
        message_text = f"{car['title']}\n - {car['price_usd']}  \n{car['link']}"
        await callback.message.answer(message_text)


def start_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Сбор данных🌐', callback_data='send_info')
            ]
        ]
    )
    return kb


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет!, {message.from_user.first_name}', reply_markup=start_kb())