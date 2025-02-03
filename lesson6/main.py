'''Работа с клавиатурой ReplyKeyboardMarkup'''

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import randrange
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher()


HELP_CMD = '''
<b>/help</b> - <em>command list</em>
<b>/start</b> - <em>command start</em>
<b>/description</b> - <em>command description bots</em>
<b>/photo</b> - <em>command photo</em>
'''


kb = ReplyKeyboardMarkup(    # создать клавиатуру
    keyboard=[
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/description'),
            KeyboardButton(text='/photo'),
        ],
        [
            KeyboardButton(text='❤️'),
            KeyboardButton(text='/orange'),
            KeyboardButton(text='/random')
        ],
    ],
    resize_keyboard=True, # размер клавиатуры
    input_field_placeholder='main menu',
    # one_time_keyboard=True #  клавиатура исчезает после нажатия на нее
)


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''реагирует на команду старт и отправляет клавиатуру'''
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome',
                           reply_markup=kb)


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    '''реагирует на команду хелп'''
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_CMD, parse_mode='HTML')


@dp.message(Command('description'))
async def cmd_descr(message: types.Message):
    '''на команду дескрипшн'''
    await bot.send_message(chat_id=message.from_user.id,
                           text='The best bot') # отправит в бота message.from_user.id


@dp.message(Command('orange'))
async def send_orange(message: types.Message): # отправит и в чат и в бота message.chat.id
    '''отправит на команду оранж фото апельсина'''
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://avatars.mds.yandex.net/i?id=b0e6c0ae549febde601ce43311c5c4787b83c7ce-10256414-images-thumbs&n=13')


@dp.message(Command('random'))
async def send_random(message: types.Message):
    '''отправит на команду рандом рандомную локацию'''
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(69),
                            longitude=randrange(70))



@dp.message()
async def send_cat(message: types.Message):
    '''Если отправлено сердечко шлет стикер'''
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAENsSxnnv9mUoa4kWCrEbHEI6iEePK9OQACTQEAAhAhAhDiOQv-uvCrtTYE')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())