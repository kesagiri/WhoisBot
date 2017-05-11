import telebot
import constants
import text


bot = telebot.TeleBot(constants.token)


# Выключает клавиатуру
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


# Различие административного и технического переносов
def handle_difference(message):
    bot.send_message(message.chat.id, text.difference, parse_mode="HTML")


# Перенос доменов
# def handle_transfer(message):
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     user_markup.row('технический', 'административный')
#     bot.send_message(message.chat.id, text.transfer, reply_markup=user_markup, parse_mode="HTML")
