import telebot
import constants
import tellDomen

bot = telebot.TeleBot(constants.token)


# Клавиатура
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help')
    bot.send_message(message.from_user.id, "Клавиатура включена. Для получения справки нажмите /help", reply_markup=user_markup)


# Выключить клавиатуру
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


# Вывод команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Я могу показать информацию о домене. Введите доменное имя:")


# Обработка сообщений и команд
@bot.message_handler(content_types=['text'])
def handle_text(message):
        bot.send_message(message.chat.id, tellDomen.domenTell(message.text))


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)

