# import telebot 
# from telebot import types

# bot = telebot.TeleBot('8320731910:AAF2GhpqvKcjQYi8wbxonzYYscGYZuDRMQw')


# @bot.message_handler(commands=['start'])
# def start(message):

#     btn1 = (types.KeyboardButton('Перейти на сайт'))
#     markup.row(btn1)
#     btn2 = (types.KeyboardButton('Видалити фото'))
#     btn3 = (types.KeyboardButton('Змінити текст'))
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'Привіт', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'Web site is open')
#     elif message.text == 'Видалити фото':
#         bot.send_message(message.chat.id, 'Deleted')

# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#      markup = types.InlineKeyboardMarkup()

#     btn1 = (types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
#     markup.row(btn1)

#     btn2 = (types.InlineKeyboardButton('Видалити фото', callback_data='delete'))
#     btn3 = (types.InlineKeyboardButton('Змінити текст', callback_data='edit'))
#     markup.row(btn2, btn3)

#     bot.reply_to(message, 'Яке гарне фото!', reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

# bot.polling(non_stop=True) 




# import telebot 
# import sqlite3

# bot = telebot.TeleBot('8320731910:AAF2GhpqvKcjQYi8wbxonzYYscGYZuDRMQw')
# name = None

# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('study.sql')
#     cur = conn.cursor()

#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()

#     bot.send_message(message.chat.id, 'Привіт, зараз тебе зареєструємо! Введи своє імя')
#     bot.register_next_step_handler(message, user_name)

# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введи пароль')
#     bot.register_next_step_handler(message, user_pass)

# def user_pass(message):
#     password = message.text.strip()

#     conn = sqlite3.connect('study.sql')
#     cur = conn.cursor()

#     cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()

#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список користувачів', callback_data='users'))
#     bot.send_message(message.chat.id, 'Користуач зареєстрований!', reply_markup=markup)
#     # bot.register_next_step_handler(message, user_pass)

# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('study.sql')
#     cur = conn.cursor()

#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()

#     info= ''
#     for el in users:
#         info += f'Імя: {el[1]}, пароль: {el[2]}\n'

#     cur.close()
#     conn.close()

#     bot.send_message(call.message.chat.id, info)

# bot.polling(non_stop=True) 