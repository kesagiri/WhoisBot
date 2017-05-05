import telebot
import constants
import tellDomen
import os
import random


bot = telebot.TeleBot(constants.token)


# Клавиатура
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help')
    user_markup.row('покажи кошака')
    bot.send_message(message.from_user.id, "Клавиатура включена. Для получения справки нажмите /help", reply_markup=user_markup)


# Выключить клавиатуру
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


# Вывод команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Я могу проконсультировать по техническому переносу домена. "
                                      "Введите доменное имя:")


# Обработка сообщений и команд
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "покажи кошака":
        directory = 'C:/Users/a.dubchak/Desktop/Cats'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
    else:
        bot.send_message(message.chat.id, tellDomen.domenTell(message.text))


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)

