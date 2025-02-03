import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API
import string
import random

bot = Bot(TOKEN_API)
dp = Dispatcher()

count = 0


@dp.message(Command('description'))
async def description(message: types.Message):
    '''описание бота'''
    await message.answer('This is description bots')
    await message.delete()


@dp.message(Command('count'))
async def check_count(message: types.Message):
    '''считает кол во отпрпавленых count'''
    global count
    await message.answer(f'count_{count}')
    count += 1


@dp.message()
async def send_random_letter(message: types.Message):
    '''отвечать на сообщение рандомной буквой'''
    await message.reply(random.choice(string.ascii_letters))

@dp.message()
async def check_zero(message: types.Message):
    '''Есть ли 0 в сообщении'''
    if '0' in message.text:
        await message.reply('YES')
    else:
        await message.reply('NO')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
