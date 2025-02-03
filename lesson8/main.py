'''Работа с клавиатурой InlineKeyboardMarkup'''

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from kbds import kb, ikb
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''реагирует на старт и выводит реплай клавиатуру'''
    await message.answer(text='welcome main menu',
                         reply_markup=kb)


@dp.message(Command('links'))
async def links_cmd(message: types.Message):
    '''реагирует на линкс и выводит инлайн клавиатуру'''
    await message.answer('select an option',
                         reply_markup=ikb)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())