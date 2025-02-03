from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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