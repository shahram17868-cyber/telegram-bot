import telebot

bot = telebot.TeleBot("توکنت_رو_اینجا_بذار")

@bot.message_handler(func=lambda m: True)
def reply(message):
    if message.text == "سلام":
        bot.reply_to(message, "سلام! ربات فعاله! 🤖")

bot.polling()
