echo import os > main.py
echo from dotenv import load_dotenv >> main.py
echo from telegram import Update, Bot >> main.py
echo from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application >> main.py
echo. >> main.py
echo load_dotenv() >> main.py
echo TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') >> main.py
echo bot = Bot(token=TOKEN) >> main.py
echo application = Application.builder().token(TOKEN).build() >> main.py
echo async def start(update: Update, context: CallbackContext) -> None: >> main.py
echo     await update.message.reply_text('Привіт! Я бот, який повторює твої повідомлення.') >> main.py
echo async def echo(update: Update, context: CallbackContext) -> None: >> main.py
echo     await update.message.reply_text(update.message.text) >> main.py
echo application.add_handler(CommandHandler('start', start)) >> main.py
echo application.add_handler(MessageHandler(filters.TEXT ^& ^~filters.COMMAND, echo)) >> main.py
echo if __name__ == '__main__': >> main.py
echo     application.run_polling() >> main.py