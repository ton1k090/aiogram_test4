'''Работа с клавиатурой InlineKeyboardMarkup'''

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randrange
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher()

ikb = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text='Button 1', url='https://youtube.com')],
        [InlineKeyboardButton(text='Button 2', url='https://youtube.com')],
    ]
)

@dp.message(Command('start'))
async def send_kb(message: types.Message):
    '''отвечает на команду старт и крепит клавиатуру'''
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello user',
                           reply_markup=ikb)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())