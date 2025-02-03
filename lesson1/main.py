import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# бот - сервер взаимодеймствия с api telegramm
TOKEN_API = '7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U' # Токен авторизации для подкл к телеграмм

bot = Bot(TOKEN_API)
dp = Dispatcher() # Отслеживать апдейты


@dp.message.handler()
async def echo(message: types.Message):
    '''просто эхо бот'''
    await message.answer(text=message.text)


@dp.message()
async def echo_upper(message: types.Message):
    '''Эхо бот отвечающий только если слов больше 1'''
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())