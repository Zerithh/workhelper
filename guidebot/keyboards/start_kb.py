from telebot import types

def start_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton('Обрати тур зі списку'),
        types.KeyboardButton('Створити новий тур')
    )
    return markup