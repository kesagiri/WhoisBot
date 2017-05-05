import telebot
import constants
import os
import random
import text
import tellDomen


bot = telebot.TeleBot(constants.token)


def handle_text(message):
    if message.text == "покажи кошака":
        directory = 'C:/Users/a.dubchak/Desktop/Cats'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, text.help, parse_mode="HTML")
    elif message.text == "Как оплатить":
        bot.send_message(message.chat.id, text.pay, parse_mode="HTML")
    elif message.text == "Перенести домен":
        bot.send_message(message.chat.id, text.transfer, parse_mode="HTML")
    elif message.text == "технический":
        bot.send_message(message.chat.id, text.tehno, parse_mode="HTML")
    elif message.text == "Технический":
        bot.send_message(message.chat.id, text.tehno, parse_mode="HTML")
    elif message.text == "тех":
        bot.send_message(message.chat.id, text.tehno, parse_mode="HTML")
    elif message.text == "административный":
        bot.send_message(message.chat.id, text.admin, parse_mode="HTML")
    elif message.text == "Административный":
        bot.send_message(message.chat.id, text.admin, parse_mode="HTML")
    elif message.text == "адм":
        bot.send_message(message.chat.id, text.admin, parse_mode="HTML")
    elif message.text == "ru":
        bot.send_message(message.chat.id, text.ru, parse_mode="HTML")
    elif message.text == "Ru":
        bot.send_message(message.chat.id, text.ru, parse_mode="HTML")
    elif message.text == "Com":
        bot.send_message(message.chat.id, text.com, parse_mode="HTML")
    elif message.text == "com":
        bot.send_message(message.chat.id, text.com, parse_mode="HTML")
    elif message.text == "Fm":
        bot.send_message(message.chat.id, text.webnames, parse_mode="HTML")
    elif message.text == "fm":
        bot.send_message(message.chat.id, text.webnames, parse_mode="HTML")
    elif message.text == "Владелец домена":
        bot.send_message(message.chat.id, text.change_adm, parse_mode="HTML")
    elif message.text == "Владелец аккаунта":
        bot.send_message(message.chat.id, text.own_account1, parse_mode="HTML")
        bot.send_message(message.chat.id, text.own_account2, parse_mode="HTML")
        directory = 'C:/Users/a.dubchak/Desktop/account1'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
        bot.send_message(message.chat.id, text.own_account3, parse_mode="HTML")
        directory = 'C:/Users/a.dubchak/Desktop/account2'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory, parse_mode="HTML")
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
        bot.send_message(message.chat.id, text.own_account4, parse_mode="HTML")
        directory = 'C:/Users/a.dubchak/Desktop/account3'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
        bot.send_message(message.chat.id, text.own_account5, parse_mode="HTML")
    elif message.text == "Восстановить пароль":
        bot.send_message(message.chat.id, text.were_password, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, "К сожалению, я не понял Вашего сообщения. Для получения справки,"
                                          "как мной управлять, нажмите /help", parse_mode="HTML")

