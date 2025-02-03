from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup

'''клавиатура главного меню старт'''
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
        [KeyboardButton(text='Random photo')],
    ],
    resize_keyboard=True,
    input_field_placeholder='main menu'
)

'''клавиатура рандом фото'''
kb_photo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='random')],
        [KeyboardButton(text='main menu')]
    ]
)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🖤', callback_data='like'),
         InlineKeyboardButton(text='👎', callback_data='dislike')],
        [InlineKeyboardButton(text='far away', callback_data='next')]
    ]
)