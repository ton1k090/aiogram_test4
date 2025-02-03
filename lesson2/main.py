import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API

HELP_COMMAND = '''
/help - list commands
/start - start bot
'''

bot = Bot(TOKEN_API)
dp = Dispatcher()


@dp.message(Command('start'))
async def help_command(message: types.Message):
    '''Реагирует на комманду старт'''
    await message.answer(text='Hello to bot')
    await message.delete()


@dp.message(Command('help'))
async def help_command(message: types.Message):
    '''Реагирует на команду хелп'''
    await message.reply(text=HELP_COMMAND)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())