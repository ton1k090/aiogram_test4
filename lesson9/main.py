'''Работа с клавиатурой InlineKeyboardMarkup callback'''

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN_API
from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


bot = Bot(TOKEN_API)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/help'), KeyboardButton(text='/vote')]
    ]
)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(text='💖', callback_data='like'),
     InlineKeyboardButton(text='🖤', callback_data='dislike')]
    ]
)


@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    '''Команда старт'''
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to bot',
                           reply_markup=kb)


@dp.message(Command('vote'))
async def vote_cmd(message: types.Message):
    '''Отпр клавиатуру и сообщение'''
    await bot.send_photo(chat_id=message.from_user.id, photo='https://avatars.mds.yandex.net/i?id=17d0f53f2a0e9837297ebc7a91e892827e966e31-12604309-images-thumbs&n=13',
                         caption='do yiu like this photo?',
                         reply_markup=ikb)
    await bot.send_message(chat_id=message.from_user.id,
                           text='')

@dp.callback_query()
async def vote_callback(callback: types.CallbackQuery): # callback - ответ на возникшее событие
    '''Отвечает в зависимости от выбора'''
    if callback.data == 'like':
        await callback.answer('You like this photo')
    await callback.answer('You dont like this photo')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())