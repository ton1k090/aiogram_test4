import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API
import string
import random

bot = Bot(TOKEN_API)
dp = Dispatcher()

HELP_COMMAND = '''
<b>/help</> - <em>commands list</em>
<b>/give</> - <em>send sticker cats</em>
<b>/start</> - <em>On bot</em>
'''


async def on_startup():
    print('I am on !')


@dp.message(Command('help'))
async def help_cmd(message: types.Message):
    '''Комана хелп с применением парс html'''
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')


@dp.message()
async def count(message: types.Message):
    '''считает сколько галочек в сообщении'''
    await message.answer(text=str(message.text.count('✅')))


@dp.message(Command('give'))
async def send_sticker(message: types.Message):
    '''Отвечает пользователю затем шлет стикер'''
    await message.answer('Look it cats ❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAENsSxnnv9mUoa4kWCrEbHEI6iEePK9OQACTQEAAhAhAhDiOQv-uvCrtTYE')


@dp.message()
async def send_sticker(message: types.Message):
    '''Отвечает пользователю yf rhfctjt cthltxrj xthysv cthltxrjv'''
    if message.text == '❤️':
        await message.answer('🖤')


async def main():
    await dp.start_polling(bot, on_startup=on_startup)

asyncio.run(main())