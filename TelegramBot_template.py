from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import numpy as np
import matplotlib.pyplot as plt

# get API token from BotFather on telegram
# define commands/conversation line like:

def start(context, update):
    update.message.reply_text('Hi, ich bin ein TelegramBot! Nutze /help, um zu sehen, was ich kann:)')

def help(context, update):
    update.message.reply_text('Nutze /entry, um mehr über mich zu erfahren!')

def main():
    updater = Updater("API-token",
                      use_context=True)
    dp = updater.dispatcher
    # conversation handler for 'real' conversations
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('entry',entry)],
        fallbacks=[],
        states={
            })
    dp.add_handler(conv_handler)
    # command handler for /commands
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# some commands:
# update.message.reply_text('your message'): send a message
# update.message.text: get last send message
# context.user_data[xy]: store parameters outside of a function
# send documents/plots/figures:
# chat_id = update.message.chat
# document = open('XY','rb')
# context.bot.send_document(chat_id, document)
