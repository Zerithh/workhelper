from keyboards.start_kb import start_kb

def register(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, 'Привіт!\nРозпочнемо роботу.\nОбери тур зі списку або створи новий.', reply_markup=start_kb())