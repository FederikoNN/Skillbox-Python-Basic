import telebot

bot = telebot.TeleBot('1961221025:AAGFfkg1arqCv1W8eyKq20CWKqnIA4wXecA')


@bot.message_handler(commands=['hello-world'])
def handle_start(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name} !')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name} !')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


bot.polling(none_stop=True, interval=0)
