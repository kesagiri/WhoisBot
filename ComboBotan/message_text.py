import telebot
import constants
import os
import random
import pasts
import viewDomen
import whois

bot = telebot.TeleBot(constants.token)


def handle_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Коничива")
    elif message.text == "покажи кошака":
        directory = 'C:/Users/a.dubchak/Desktop/Cats'
        all_files_in_this_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_this_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
        # Отправка аудио
        # directory_myau = 'C:/Users/a.dubchak/Desktop/Myau'
        # all_files_in_this_directory_myau = os.listdir(directory_myau)
        # random_audio = random.choice(all_files_in_this_directory_myau)
        # voice = open(directory_myau + '/' + random_audio, 'rb')
        # bot.send_chat_action(message.from_user.id, "upload_voice")
        # bot.send_voice(message.from_user.id, voice)
        # voice.close()
    elif message.text == "домен":
        bot.send_message(message.chat.id, pasts.isExactly)
    elif message.text == "договор":
        bot.send_message(message.chat.id, pasts.agreement)
    elif message.text == "Технический перенос":
        bot.send_message(message.chat.id, pasts.tehDomen)
    elif message.text == "Административный перенос":
        bot.send_message(message.chat.id, pasts.admDomen)
    elif message.text == "whois":
        bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, message.text)
    else:
        bot.send_message(message.chat.id, "Научись внятно объяснять, что тебе нужно")

