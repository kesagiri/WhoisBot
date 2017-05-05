import os
import random
import telebot
import constants
import tellDomen
import text
import message_text


bot = telebot.TeleBot(constants.token)


# Клавиатура
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Помощь', 'Как оплатить')
    user_markup.row('Перенести домен', 'Владелец домена')
    user_markup.row('Владелец аккаунта', 'Восстановить пароль')
    user_markup.row('покажи кошака')
    bot.send_message(message.from_user.id, text.start, reply_markup=user_markup)


# Выключить клавиатуру
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


# Вывод команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, text.start, parse_mode="HTML")


# Вывод команды /different
@bot.message_handler(commands=['difference'])
def handle_help(message):
    bot.send_message(message.chat.id, text.difference, parse_mode="HTML")


# Обработка сообщений и команд
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message_text.handle_text(message)


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)

