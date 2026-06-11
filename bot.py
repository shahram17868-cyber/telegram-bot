import telebot

bot = telebot.TeleBot("8818489067:AAFOY49RuH0LWvjPi3HHlpftvR5OlTmj1b8")

@bot.message_handler(func=lambda m: True)
def reply(message):
    if message.text == "سلام":
        bot.reply_to(message, "سلام! ربات فعاله! 🤖")

bot.polling()
