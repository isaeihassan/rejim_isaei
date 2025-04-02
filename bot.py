import telebot
import os

TOKEN = os.getenv("TOKEN")  # دریافت توکن از متغیر محیطی

if not TOKEN:
    raise ValueError("❌ خطا: توکن تنظیم نشده است!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به بات رژیم غذایی و ورزشی خوش آمدی! 😊")

bot.polling()
