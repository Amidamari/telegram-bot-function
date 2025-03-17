import os
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application

# Зчитуємо змінну середовища TELEGRAM_BOT_TOKEN
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привіт! Я бот, який повторює твої повідомлення.')

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

if __name__ == '__main__':
    application.run_polling()
    