'''Работа с клавиатурой'''

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(    # создать клавиатуру
    keyboard=[
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/description'),
            KeyboardButton(text='/photo'),
        ]
    ],
    resize_keyboard=True, # размер клавиатуры
    input_field_placeholder='main menu',
    # one_time_keyboard=True #  клавиатура исчезает после нажатия на нее
)


HELP_CMD = '''
<b>/help</b> - <em>command list</em>
<b>/start</b> - <em>command start</em>
<b>/description</b> - <em>command description bots</em>
<b>/photo</b> - <em>command photo</em>
'''


@dp.message(Command('help'))
async def help_cmd(message: types.Message):
    '''обрабатывает команду help'''
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_CMD,
                           parse_mode='HTML',
                           reply_markup=ReplyKeyboardRemove()) # удалит клавиатуру с экрана
    await message.delete() # удалять команду с чата после написания


@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    '''обрабатывает команду start'''
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to bot',
                           parse_mode='HTML',
                           reply_markup=kb) # добавить клавиатуру
    await message.delete()


@dp.message(Command('description'))
async def description_cmd(message: types.Message):
    '''обрабатывает команду description'''
    await bot.send_message(chat_id=message.from_user.id, text='description bot', parse_mode='HTML')
    await message.delete()


@dp.message(Command('photo'))
async def photo_cmd(message: types.Message):
    '''обрабатывает команду photo'''
    await bot.send_photo(message.from_user.id, photo='https://avatars.mds.yandex.net/i?id=578064b13d7a06e7ffd326bce4c9cac231addcb4-5325046-images-thumbs&n=13')
    await message.delete()


async def main():
    await dp.start_polling(bot)

asyncio.run(main())