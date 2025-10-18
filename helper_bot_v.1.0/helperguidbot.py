import telebot
from telebot import types
import os
import json
from datetime import datetime


bot = telebot.TeleBot('7557698573:AAFgiW-yRwLkk8X4lrDY-IWaI_lrg7nGvJE')

EXPENSES_FILE = 'expenses.json'

CASH_FILE = 'cash.json'

def load_cash():
    if os.path.exists(CASH_FILE):
        try: 
            with open(CASH_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
            'cash' : 0.0,
            'card' : 0.0,
            'total' : 0.0,
            'cash_today' : 0.0,
            'card_today' : 0.0,
            'total_today' : 0.0

        }

def save_cash(cash_data):
    with open(CASH_FILE, 'w', encoding='utf-8') as f:
        json.dump(cash_data, f, ensure_ascii=False, indent=2)

CASH_HISTORY_FILE = 'cash_history.json'

def load_cash_history():
    if os.path.exists(CASH_HISTORY_FILE):
        with open(CASH_HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cash_history(history):
    with open(CASH_HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def update_cash_history(cash_amount, card_amount):
    history = load_cash_history()
    today = datetime.now().strftime('%y-%m-%d')

    if today not in history:
        history[today] = {'cash' : 0.0, 'card' : 0.0}

    history[today]['cash'] += cash_amount
    history[today]['card'] += card_amount

    save_cash_history(history)

@bot.message_handler(commands=['show_sum'])
def show_sum_command(message):
    user_id = message.from_user.id

    cash_data = load_cash()
    total_cash = cash_data.get('cash', 0.0)
    total_card = cash_data.get('card', 0.0)
    total_sum = total_cash + total_card

    today = datetime.now().strftime('%y-%m-%d')
    history = load_cash_history()
    today_data = history.get(today, {'cash' : 0.0, 'card' : 0.0})
    today_cash = today_data.get('cash', 0.0)
    today_card = today_data.get('card', 0.0)
    today_sum = today_cash + today_card

    message_text = (
        f"💼 *Загальний стан каси:*\n"
        f"Готівка: {total_cash:.2f} €\n"
        f"Карта: {total_card:.2f} €\n"
        f"Разом: {total_sum:.2f} €\n\n"
        f"📅 *Каса за сьогодні* ({today}):\n"
        f"Готівка: {today_cash:.2f} €\n"
        f"Карта: {today_card:.2f} €\n"
        f"Разом: {today_sum:.2f} €"
    )

    bot.send_message(message.chat.id, message_text)

def get_keyboard_1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Екскурсія')
    btn2 = types.KeyboardButton('Навушники')
    btn3 = types.KeyboardButton('City Tax')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт!\n\nРозпочнемо роботу?\n\nНижче виберіть що будемо записувати)', reply_markup=get_keyboard_1())

user_state = {}

@bot.message_handler(func=lambda message: message.text in ['Екскурсія', 'Навушники', 'City Tax'])
def selection_step(message):
    user_id = message.from_user.id
    user_state[user_id] = {
        'mode' : message.text,
        'step' : 'awaiting_price'
    }

    bot.send_message(message.chat.id, f'Вкажіть ціну за одиницю для "{message.text}": ')

@bot.message_handler(func=lambda message: message.from_user.id in user_state and user_state[message.from_user.id]['step'] == 'awaiting_price')
def selection_price(message):
    global user_state
    user_id = message.from_user.id
    text = message.text.replace(',', '.')

    try:
        price = float(text)
        user_state[user_id]['price'] = price
        user_state[user_id]['step'] = 'awaiting_quantity'

        bot.send_message(message.chat.id, 'Яка кількість?')
    except ValueError:
        bot.send_message(message.chat.id, 'Введіть коректну ціну (наприклад 25.5)')

def get_payment_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('💵 Усі готівкою')
    btn2 = types.KeyboardButton('💳 Усі картою')
    btn3 = types.KeyboardButton('↔️ Розділити оплату')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup


def get_keyboard_2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('Так'), types.KeyboardButton('Ні'))
    return markup

@bot.message_handler(func=lambda message: message.from_user.id in user_state and user_state[message.from_user.id]['step'] == 'awaiting_quantity')
def selection_quantity(message):
    global user_state

    user_id = message.from_user.id
    text = message.text.strip()

    if not text.isdigit():
        bot.send_message(message.chat.id, 'Введіть ціле число (наприклад 3)')
        return
    
    quantity = int(text)
    user_state[user_id]['quantity'] = quantity 
    price = user_state[user_id]['price']
    mode = user_state[user_id]['mode']
    total = quantity * price

    user_state[user_id]['step'] = 'awaiting_payment_method'

    bot.send_message(message.chat.id, 'Як будуть оплачувати?', reply_markup=get_payment_keyboard())

def show_final_summary(message):
    user_id = message.from_user.id
    state = user_state.get(user_id, {})

    mode = state.get('mode')
    price = state.get('price')
    quantity = state.get('quantity')
    card_count = state.get('payment', {}).get('card', 0)
    cash_count = state.get('payment', {}).get('cash', 0)

    card_sum = card_count * price
    cash_sum = cash_count * price
    total_sum = quantity * price

    cash_data = load_cash()
    cash_data['cash'] += cash_sum
    cash_data['card'] += card_sum
    cash_data['total'] += total_sum

    cash_data['cash_today'] += cash_sum
    cash_data['card_today'] += card_sum
    cash_data['total_today'] += total_sum
    save_cash(cash_data)
    update_cash_history(cash_sum, card_sum)

    summary = f'📋 Звіт по продажу: "{mode}"\n' 
    summary += f'Загальна кількість чоловік - {quantity}\n\n'
    summary += f'💳 Картою: {card_count} чол. на суму: {card_sum:.2f} €\n'
    summary += f'💵 Готівкою: {cash_count} чол. на суму: {cash_sum:.2f} €\n\n'
    summary += f'💰 *Разом: {total_sum:.2f} €\n\n'

    summary += '📦 *Поточний стан каси:*\n'
    summary += f'💳 Усього карткою: {cash_data['card']:.2f} €\n'
    summary += f'💵 Усього готівкою: {cash_data['cash']:.2f} €\n'
    summary += f'💰 Загалом: {cash_data['total']:.2f} €\n'

    bot.send_message(message.chat.id, summary)

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)

def add_expense_to_system(description, amount):
    cash_data = load_cash()
    expenses = load_expenses()

    cash_data['cash_today'] -= amount
    cash_data['total_today'] -= amount
    cash_data['cash'] -= amount
    cash_data['total'] -= amount

    expense_entry = {
        'description' : description,
        'amount' : amount,
        'timestamp' : datetime.now().strftime('%y-%m-%d, %H:%M:%S')
    }

    expenses.append(expense_entry)

    save_cash(cash_data)
    save_expenses(expenses)
    update_cash_history(-amount, 0)

    return cash_data, expense_entry, expenses


def build_cash_report():
    cash_data = load_cash()
    expenses = load_expenses()
    report = (
        f"💼 *Загальний стан каси:*\n"
        f"Готівка: {cash_data['cash']:.2f} €\n"
        f"Карта: {cash_data['card']:.2f} €\n"
        f"Разом: {cash_data['total']:.2f} €\n\n"
    )

    if expenses:
        report += '📉 *Витрати:*\n'
        for e in expenses[-5:]:
            report += f'{e['description']}: -{e['amount']:.2f} €\n'
    return report

def reset_expenses():
    save_expenses([])

@bot.message_handler(commands=['reset_expenses'])
def handle_reset_expenses(message):
    reset_expenses()
    bot.send_message(message.chat.id, '🗑️ Всі витрати були очищені')

@bot.message_handler(commands=['reset_today'])
def reset_today(message):
    today = datetime.now().strftime('%y-%m-%d')
    user_id = message.from_user.id
    cash_data = load_cash()

    cash_data['cash_today'] = 0.0
    cash_data['card_today'] = 0.0
    cash_data['total_today'] = 0.0
    save_cash(cash_data)

    history = load_cash_history()
    if today in history:
        del history[today]
        save_cash_history(history)

    bot.send_message(message.chat.id, '✅ Каса за останню добу була скинута')

@bot.message_handler(commands=['reset_all'])
def reset_all(message):
    user_id = message.from_user.id
    cash_data = {
        'cash': 0.0,
        'card': 0.0,
        'total': 0.0,
        'cash_today': 0.0,
        'card_today': 0.0,
        'total_today': 0.0
    }
    save_cash(cash_data)
    save_cash_history({})
    bot.send_message(message.chat.id, '⚠️ Вся каса була скинута до 0.')

@bot.message_handler(commands=['add_calculation'])
def add(message):
    bot.send_message(message.chat.id, 'Що ще додамо?', reply_markup=get_keyboard_1())

expense_state = {}

@bot.message_handler(commands=['add_costs'])
def add_costs(message):
    user_id = message.from_user.id
    expense_state[user_id] = {'step' : 'awaiting_description'}
    bot.send_message(message.chat.id, '✏️ Введи назву витрати:')

@bot.message_handler(func=lambda message: message.from_user.id in expense_state and expense_state[message.from_user.id]['step'] == 'awaiting_description')
def handle_expens_description(message):
    user_id = message.from_user.id
    description = message.text.strip()

    if not description:
        bot.send_message(message.chat.id, '❗ Опис не може бути порожнім. Спробуй ще раз.')
        return
    
    expense_state[user_id]['description'] = description
    expense_state[user_id]['step'] = 'awaiting_amount'
    bot.send_message(message.chat.id, '💶 Введи суму витрати (наприклад: 25.50):')

@bot.message_handler(func=lambda message: message.from_user.id in expense_state and expense_state[message.from_user.id]['step'] == 'awaiting_amount')
def handle_expense_amount(message):
    cash_data = load_cash()
    user_id = message.from_user.id
    amount_text = message.text.strip().replace(',', '.')

    try:
        amount = float(amount_text)
        if amount <0:
            raise ValueError('Сума має бути більшою за 0')
    except ValueError:
        bot.send_message(message.chat.id, '❗ Введи коректну суму у форматі 25.50')
        return
    
    description = expense_state[user_id]['description']
    cash_data, expense_entry, all_expenses = add_expense_to_system(description, amount)

    report = build_cash_report()

    bot.send_message(message.chat.id, f'✅ Витрату додано:\n\n📌 {description}\n💶 {amount:.2f} €')
    bot.send_message(message.chat.id, report)

    del expense_state[user_id]    
                     

@bot.message_handler(func=lambda message: message.from_user.id in user_state and user_state[message.from_user.id]['step'] == 'awaiting_payment_method')
def selection_payment_method(message):
    user_id = message.from_user.id
    method = message.text.strip()

    if method == '💵 Усі готівкою':
        user_state[user_id]['payment'] = {'cash' : user_state[user_id]['quantity'], 'card' : 0}
        show_final_summary(message)
    elif method == '💳 Усі картою':
        user_state[user_id]['payment'] = {'cash' : 0, 'card' : user_state[user_id]['quantity']}
        show_final_summary(message)
    elif method == '↔️ Розділити оплату':
        user_state[user_id]['step'] = 'awaiting_card_count'
        bot.send_message(message.chat.id, 'Скільки людей платять картою?', parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, 'Будь ласка, вибери варіант з клавіатури')

@bot.message_handler(func=lambda message: message.from_user.id in user_state and user_state[message.from_user.id]['step'] == 'awaiting_card_count')
def selection_card_count(message):
    user_id = message.from_user.id
    text = message.text.strip()

    if not text.isdigit():
        bot.send_message(message.chat.id, 'Введіть число (наприклад 3)')
        return
    card_count = int(text)
    quantity = user_state[user_id].get('quantity')

    if card_count > quantity:
        bot.send_message(message.chat.id, f'Загальна кількість - {quantity}. Введіть число не більше')
        return
    user_state[user_id]['payment'] = {
        'card' : card_count,
        'cash' : quantity - card_count
    }
    user_state[user_id]['step'] = None

    show_final_summary(message)


bot.polling(non_stop=True, interval=0, timeout=20)