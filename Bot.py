import telebot

# Bot token from Telegram
TOKEN = "7648930587:AAHcDBywHNRXhYQmVSc9HIWN4dE52Ekczsg"

bot = telebot.TeleBot(TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Hello! Bot is working perfectly.")

# Keep the bot running
bot.polling(none_stop=True)
