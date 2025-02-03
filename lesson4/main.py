import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API
import string
import random

bot = Bot(TOKEN_API)
dp = Dispatcher()

HELP_COMMAND = '''
/help - list commands
/start - start bot
'''

@dp.message(Command('help'))
async def help_command(message: types.Message):
    '''отправляет в личку ответ'''
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND)
    await message.delete()


@dp.message(Command('photo'))
async def send_image(message: types.Message):
    '''отправить фото в ответ в бота'''
    await bot.send_photo(chat_id=message.chat.id, photo='https://avatars.mds.yandex.net/i?id=1cef78225f9275cb035ab2c8e7ad2f0b773643e8-4865547-images-thumbs&n=13')
    await message.delete()


@dp.message(Command('location'))
async def send_point(message: types.Message):
    '''отправить локацию в бота'''
    await bot.send_location(chat_id=message.from_user.id, latitude=55, longitude=74)
    await message.delete()



@dp.message
async def echo(message: types.Message):
    '''echo'''
    # await message.answer(message.text) # отправит туда куда написал юзер
    await bot.send_message(chat_id=message.chat.id, text='hello') # отправить туда куда написал юзер


async def main():
    await dp.start_polling(bot)

asyncio.run(main())