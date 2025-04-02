import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تنظیمات logging برای ثبت ارورها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('سلام! من بات تلگرام شما هستم.')

# دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('برای راهنمایی بیشتر با من صحبت کن.')

# تعریف تابع main برای راه‌اندازی بات
async def main():
    # توکن بات تلگرام خود را از BotFather وارد کنید
    TELEGRAM_TOKEN = '7639099981:AAEZDr8_6uRDOCi0M75tzHbBjDqu5ptxin4'
    
    # ایجاد Application به جای Updater
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # اضافه کردن هندلرها برای دستورهای /start و /help
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # شروع بات و منتظر بودن برای پیام‌ها
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
