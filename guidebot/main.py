import telebot
from telebot import TeleBot
from handlers import start_handler
from services.db import init_db
init_db()


bot = TeleBot('8378613185:AAEkYMNsF7GFVcB6fiFJELFMmxqX32RwUHU', parse_mode='HTML')

start_handler.register(bot)

print('Бот запущено!')

bot.infinity_polling()