import telebot
import os

# Environment variable se token lena — secure method
TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Hello! Bot is working perfectly.")

bot.polling(none_stop=True)
