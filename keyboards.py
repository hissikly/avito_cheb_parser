from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup


cut_titles = []


def start_kb():
    start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('/today')
    button2 = KeyboardButton('/tommorow')
    start_kb.add(button1, button2)
    return start_kb


def create_keyboard(dt_lst):
    kb = InlineKeyboardMarkup(row_width=len(dt_lst))
    for el in dt_lst:
        if el[:20] != el:
            success_el = el[:17] + "..."
        else:
            success_el = el
        cut_titles.append(success_el)
        button = InlineKeyboardButton(text=success_el, callback_data=success_el)
        kb.add(button)
    return kb
