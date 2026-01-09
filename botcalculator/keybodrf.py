from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='+'),KeyboardButton(text='-')],
    [KeyboardButton(text='*'),KeyboardButton(text='/')],
], resize_keyboard=True)