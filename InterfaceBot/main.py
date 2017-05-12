import os
import random
import telebot
import constants
import text
import message_text
import commands
import whois
import json
import tell_domain


bot = telebot.TeleBot(constants.token)


# Клавиатура
@bot.message_handler(commands=['start'])
def handle_text(message):
    # user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    # user_markup.row('Помощь', 'Как оплатить')
    # user_markup.row('Перенести домен', 'Владелец домена')
    # user_markup.row('Владелец аккаунта', 'Восстановить пароль')
    # user_markup.row('покажи кошака')
    # add 'reply_markup=user_markup' for turn on keyboards
    bot.send_message(message.from_user.id, text.start, parse_mode="HTML")


# Выключить клавиатуру
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    commands.handle_stop(message)


# Вывод команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, text.help, parse_mode="HTML")


# Вывод команды /whois
@bot.message_handler(commands=['whois'])
def handle_help(message):
    who = bot.send_message(message.chat.id, text.whois, parse_mode="HTML")
    bot.register_next_step_handler(who, domain_tell)


def domain_tell(message):
    bot.send_message(message.chat.id, tell_domain.domain_tell(message.text), parse_mode="HTML")


# Вывод команды по различию доменов /different
@bot.message_handler(commands=['difference'])
def handle_difference(message):
    dif = bot.send_message(message.chat.id, text.difference, parse_mode="HTML")
    bot.register_next_step_handler(dif, domain_zone)


# Вывод команды по различию доменов /pay
@bot.message_handler(commands=['pay'])
def handle_help(message):
    bot.send_message(message.chat.id, text.pay, parse_mode="HTML")


# Вывод команды по различию доменов /change_admin
@bot.message_handler(commands=['change_admin'])
def handle_help(message):
    bot.send_message(message.chat.id, text.change_adm, parse_mode="HTML")


# Вывод команды по различию доменов /domain_transfer
@bot.message_handler(commands=['domain_transfer'])
def handle_transfer(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.add(*[telebot.types.KeyboardButton(name) for name in ['административный', 'технический']])
    msg = bot.send_message(message.chat.id, text.transfer, reply_markup=user_markup, parse_mode="HTML")
    bot.register_next_step_handler(msg, name)


# При выполнении команды domain_transfer, выполняется def name
def name(message):
    if message.text == "административный":
        user_markup = telebot.types.InlineKeyboardButton()
        user_markup.add(*[telebot.types.InlineKeyboardButton(text=zone, callback_data=zone)
                          for zone in ['ru', 'com', 'fm']])
        adm = bot.send_message(message.chat.id, text.admin, reply_markup=user_markup, parse_mode="HTML")
        # bot.register_next_step_handler(adm, domain_zone)
    elif message.text == "технический":
        bot.send_message(message.chat.id, text.tehno, parse_mode="HTML")


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'ru':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message.id, text=text.ru, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(c.from_user.id, "Если у Вас остались дополнительные вопросы, "
                                               "нажмите /help", reply_markup=hide_markup)
    elif c.data == 'com':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message.id, text=text.com, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(c.from_user.id, "Если у Вас остались дополнительные вопросы, "
                                         "нажмите /help", reply_markup=hide_markup)
    elif c.data == 'fm':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message.id, text=text.fm, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(c.from_user.id, "Если у Вас остались дополнительные вопросы, нажмите /help", reply_markup=hide_markup)


def domain_zone(message):
    if message.text == "ru":
        bot.send_message(message.chat.id, text.ru, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Если у Вас остались дополнительные вопросы, "
                                               "нажмите /help", reply_markup=hide_markup)
    elif message.text == "com":
        bot.send_message(message.chat.id, text.com, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Если у Вас остались дополнительные вопросы, "
                                               "нажмите /help", reply_markup=hide_markup)
    elif message.text == "fm":
        bot.send_message(message.chat.id, text.webnames, parse_mode="HTML")
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Если у Вас остались дополнительные вопросы, "
                                               "нажмите /help", reply_markup=hide_markup)


# Вывод команды по различию доменов /account
@bot.message_handler(commands=['account'])
def handle_help(message):
    bot.send_message(message.chat.id, text.own_account1, parse_mode="HTML")


# Вывод команды по различию доменов /different
@bot.message_handler(commands=['return_account'])
def handle_help(message):
    bot.send_message(message.chat.id, text.were_password, parse_mode="HTML")


# Обработка сообщений и команд
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message_text.handle_text(message)


bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)

