from transliterate import to_latin, to_cyrillic
import telebot

TOKEN ="1909623145:AAEkjGuoBlRi1_aArYX560ZgFQD87hzLKGE"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum,siz Lotin-Kiril botdasiz!"
    javob+="\nMatn kiriting"
    bot.reply_to(message, javob )

@bot.message_handler(func=lambda m: True)
def echo(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


bot.polling()