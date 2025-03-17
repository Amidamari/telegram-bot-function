import os
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application

load_dotenv()
TOKEN = os.getenv('7243782435:AAFdWdi55hF0k3GBA3wpJK59zZxdAoEnFeE')
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