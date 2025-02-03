import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from config import TOKEN_API

from first_project.keyboards import kb, kb_photo, ikb

bot = Bot(TOKEN_API)
dp = Dispatcher()

HELP_CMD = '''
<b>/help</b> - <em>command list</em>
<b>/start</b> - <em>command start</em>
<b>/description</b> - <em>command description bots</em>
<b>/photo</b> - <em>command photo</em>
'''

arr_photos = [
    'https://avatars.mds.yandex.net/i?id=299399c24aa1a33472bdfe8838696e8d_l-5173358-images-thumbs&n=13',
    'https://avatars.mds.yandex.net/i?id=41b11c36f25224a8d68444b567a9cff8_sr-12527814-images-thumbs&n=13',
    'https://www.dhresource.com/0x0/f2/albu/g6/M00/34/F3/rBVaSFtQMnOAdQNiAACipkisWis447.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/41eWsodFBhL.jpg',
]

photos = dict(zip(arr_photos, ['one_photo', 'two photo', 'three photo', 'four photo'])) # сшиваем два массива и получаем словарь ключи ссылки значения номера - названия


async def send_random(message: types.Message):
    '''Отпр рандом фото и крепит клавиатуру инлайн'''
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,  # отправляем рандом фото
                         caption=photos[random_photo],
                         reply_markup=ikb)  # привязали описание к фото


@dp.message(F.text == 'Random photo')
async def kbd_photo(message: types.Message):
    '''Реагирует на Random photo и отправляет клавиатуру'''
    await message.answer(text='input random',
                         reply_markup=kb_photo
                         )
    await message.delete()


@dp.message(F.text == 'random')
async def send_random(message: types.Message):
    '''Отправляет рандомное фото по команде random'''
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,  # отправляем рандом фото
                         caption=photos[random_photo],
                         reply_markup=ikb)  # привязали описание к фото


@dp.message(F.text == 'main menu')
async def open_kb(message: types.Message):
    '''Открывает главное меню'''
    await message.answer(text='main menu welcome',
                         reply_markup=kb
                         )
    await message.delete()



@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''Команда старт и клавиатура'''
    await message.answer(text='Welcome to bot',
                         reply_markup=kb)
    await message.delete() # удалить текст старт с чата

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    '''Команда хелп и список команд'''
    await message.answer(text=HELP_CMD,
                         parse_mode='HTML')
    await message.delete()  # удалить текст хелп с чата


@dp.message(Command('description'))
async def cmd_description(message: types.Message):
    '''Команда описание и стикер'''
    await message.answer(text='Welcome to bot this is the best')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAENsLtnnlknRB3nehDAD7RRhBwjbGt4_QACWAIAArrAlQUQtZZnn0DJWjYE')#  отправлять откуда запрошено
    await message.delete()  # удалить текст дескрипшн с чата



@dp.callback_query()
async def callback_photo(callback: types.CallbackQuery):
    '''отвечает в зависимости от выбраной кнопки'''
    if callback.data == 'like':
        await callback.answer('Your cool man')
    elif callback.data == 'dislike':
        await callback.answer('Bad man')
    else:
        await send_random(message=callback.message)
        await callback.answer()


async def main():
    await dp.start_polling(bot)

asyncio.run(main())