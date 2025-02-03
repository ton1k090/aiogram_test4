from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

'''Файл с клавиатурами'''

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='youtube', url='https://yiutube.com'),
            InlineKeyboardButton(text='google', url='https://google.com')
        ]
    ]
)


kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/links')]
    ]
)