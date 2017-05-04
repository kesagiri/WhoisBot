import telebot
import constants
import message_text
import keyboard
import helpBot


bot = telebot.TeleBot(constants.token)


# Клавиатура
@bot.message_handler(commands=['start'])
def handle_text(message):
    keyboard.handle_text(message)


# Выключить клавиатуру
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    keyboard.hide_markup(message)


# Вывод команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, helpBot.helpBot)


# Обработка сообщений и команд
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message_text.handle_text(message)


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)
