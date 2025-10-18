# import telebot
# from telebot import types

# bot = telebot.TeleBot('8320731910:AAF2GhpqvKcjQYi8wbxonzYYscGYZuDRMQw')
    

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Видалити фото')
#     btn3 = types.KeyboardButton('Змінити текст')
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'Привіт', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'Website id open')
#     elif message.text == 'Видалити фото':
#         bot.send_message(message.chat.id, 'Deleted')


# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='google.com')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Видалити фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Змінити текст', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Яке гарне фото!', reply_markup=markup)

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

# bot.polling(non_stop=True)




import telebot
from telebot import types
import json
import os


bot = telebot.TeleBot('8320731910:AAF2GhpqvKcjQYi8wbxonzYYscGYZuDRMQw')


def get_shift_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(
    types.KeyboardButton("Ранкова"),
    types.KeyboardButton("Денна"),
    types.KeyboardButton("Нічна")
)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго дня!\nНа якій ви зміні?', reply_markup=get_shift_keyboard())

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
        

@bot.message_handler(commands=['tasks'])
def tasks(message):
    user_id = str(message.from_user.id)
    data = load_json('data.json')


    if user_id not in data or 'shift' not in data[user_id]:
        bot.send_message(message.chat.id, 'Ти ще не вибрав зміну.\nНатисни /start')
        return
    
    shift = data[user_id]['shift'] # поміщаємо у змінну звернення до словника (data) за ключем user_id та shift (щоб знайти значення shift)

    tasks_by_shift = load_json("tasks.json") # команда load_json перетворює json у Python словник
    tasks = tasks_by_shift.get(shift) # дістаємо задачі для зміни яку обрав користувач


    if not tasks:
        bot.send_message(message.chat.id, f'Немає задач для зміни: "{shift}" ')
        return
    
    done = data[user_id].get('done', [])

    text = f'Завдання для зміни "{shift}"\n\n'
    for i, task in enumerate(tasks, 1): # перебирає список та додає номери
        status = '✅' if (i - 1) in done else '⬜'
        text += f'{i}. {status} {task}\n'

    bot.send_message(message.chat.id, text, parse_mode='Markdown')

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@bot.message_handler(func=lambda message: message.text in ['Ранкова', 'Денна', 'Нічна'])
def handle_shif_selection(message):
    user_id = str(message.from_user.id)
    data = load_json('data.json')

    data[user_id] = {
        'shift': message.text,
        'done': []
    }

    save_json('data.json', data)

    bot.send_message(message.chat.id, f'Зміна "{message.text}" збережена.\nНапиши /tasks щоб переглянути завдання.')

@bot.message_handler(commands=['done'])
def mark_done(message):
    parts = message.text.strip().split()

    if len(parts) != 2 or not parts[1].isdigit():
        bot.send_message(message.chat.id, 'Формат команди: /done <номер>')
        return
    
    task_index = int(parts[-1]) - 1

    user_id = str(message.from_user.id)
    data = load_json('data.json')

    if user_id not in data or 'shift' not in data[user_id]:
        bot.send_message(message.chat.id, 'Спочатку вибери зміну командою "/start"')
        return

    shift = data[user_id]['shift']

    tasks = load_json('tg/tasks.json').get(shift)

    if not tasks:
        bot.send_message(message.chat.id, f'Немає задач для зміни: "{shift}"')
        return
    
    if task_index < 0 or task_index >= len(tasks):
        bot.send_message(message.chat.id, 'Не правильний номер завдання')
        return
    
    if 'done' not in data[user_id]:
        data[user_id]['done'] = []

    if task_index in data[user_id]['done']:
        bot.send_message(message.chat.id, 'Це завдання позначене як виконане')
        return
    
    data[user_id]['done'].append(task_index)
    save_json('data.json', data)

    bot.send_message(message.chat.id, f'Завдання №{task_index + 1} позначено як виконане')

@bot.message_handler(commands=['reset'])
def reset_tasks(message):
    user_id = str(message.from_user.id)
    data = load_json('data.json')

    if user_id not in data or 'shift' not in data[user_id]:
        bot.send_message(message.chat.id, 'Спочатку вибери зміну командою: "/start"')
        return
    
    data[user_id]['done'] = []
    save_json('data.json', data)

    bot.send_message(message.chat.id, '✅ Список виконаних завдань очищено!')

@bot.message_handler(commands=['add'])
def add_task(message):
    user_id = str(message.from_user.id)
    data = load_json('data.json')

    if user_id not in data or 'shift' not in data[user_id]:
        bot.send_message(message.chat.id, 'Спочатку вибери зміну командою: "/start"')
        return

    

bot.polling(non_stop=True)



