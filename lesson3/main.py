import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API
import string
import random

bot = Bot(TOKEN_API)
dp = Dispatcher()


async def on_startup(_):
    print('Bot on!')

@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    '''Отвечает на команду старт'''
    await message.answer('<em>Hello! Welcome</em>', parse_mode='HTML') # Парс мод для добавления тегов стилистики


@dp.message(Command('give'))
async def start_cmd(message: types.Message):
    '''Отвечает на команду give стикером стикеры брать в get stiker id боте'''
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAENsLtnnlknRB3nehDAD7RRhBwjbGt4_QACWAIAArrAlQUQtZZnn0DJWjYE') # отправляем в чат который юзером открыт
    await message.delete() # удалить команду из чата


async def main():
    await dp.start_polling(bot, on_startup=on_startup)

asyncio.run(main())
