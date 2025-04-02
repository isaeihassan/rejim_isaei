import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# تنظیمات logging برای ثبت ارورها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من بات تلگرام شما هستم.')

# دستور /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('برای راهنمایی بیشتر با من صحبت کن.')

# تعریف تابع main برای راه‌اندازی بات
def main():
    # توکن بات تلگرام خود را از BotFather وارد کنید
    TELEGRAM_TOKEN = '7639099981:AAEZDr8_6uRDOCi0M75tzHbBjDqu5ptxin4'
    
    # ایجاد Updater و Dispatcher
    updater = Updater(TELEGRAM_TOKEN)

    # گرفتن دیسپیچر
    dispatcher = updater.dispatcher

    # اضافه کردن هندلرها برای دستورهای /start و /help
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # شروع بات و منتظر بودن برای پیام‌ها
    updater.start_polling()

    # ادامه دادن بات تا زمانی که کاربر آن را متوقف کند
    updater.idle()

if __name__ == '__main__':
    main()
