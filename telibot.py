from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = "6656824871:AAFKeTgFifUCrxttvwLa_du4Lld0881tjA0"

BOT_USERNAME: Final = '@INF3CTED_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi My self INF3CTED!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi there! I'm INF3CTED, your friendly Telegram bot.\n"
        "You can use the following commands:\n"
        "/start - Start interacting with the bot\n"
        "/help - Display this help message\n"
        "Feel free to send me any message, and I'll echo it back to you!")
    







def handle_response(text:str)->str:
        processed: str = text.lower()

        if'hello' in processed:
            return 'Hey there!'
        
        if'Hi how aree you' in processed:
            return 'Im fine!'
        
        return 'I do not understand!'
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.text
    text = update.message.text
    # response = handlee_responses(text)
    # await update.message.reply_text(response)  



    print(f'User ({update.message.chat.id})in {message_type}:"{text}"')

    if message_type == 'group':
      if BOT_USERNAME in text:
        new_text:str= text.replace(BOT_USERNAME,'').strip()
        response:str = handle_response(new_text)
      else:
        return
    
    else:
      response:str = handle_response(text)

    print('bot:',response)
    await update.message.reply_text(response)


async def error_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error "{context.error}"')  

if __name__ == '__main__':
    print('Starting bot...')
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_callback)
    print('running bot...')
    application.run_polling()        
