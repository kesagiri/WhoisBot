import telebot
import constants


bot = telebot.TeleBot(constants.token)


def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help', 'whois')
    user_markup.row('Технический перенос')
    user_markup.row('Административный перенос')
    # user_markup.row('домен', 'договор')
    user_markup.row('покажи кошака')
    bot.send_message(message.from_user.id, "Клавиатура включена. Для получения справки нажмите /help", reply_markup=user_markup)


def hide_markup(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start",
                     reply_markup=hide_markup)
