from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import praw
import os
import urllib
import pandas as pd
import datetime

# get API token from BotFather on telegram
# define commands/conversation line like:

# defining conversation states
NAME, SUBJECT, FOOD = range(3)

def start(update, context):
    update.message.reply_text('Hi, ich bin ein TelegramBot! Nutze /hallo, um zu sehen, was ich kann:)')

def hallo(update, context):
    update.message.reply_text('''
Hallo! Ich bin ein Bot und du kannst einige Commands nutzen, um mit mir zu interagieren!
/tictactoe: Hier kannst du gegen mich TicTacToe spielen!
/chat: Wir können auch ein bisschen quatschen!
/memes: Die besten Memes aller Zeiten''')

def chat(update, context):
    update.message.reply_text('Okay, erzähl mir was über dich! Wie heißt du?')
    return NAME

def name(update, context):
    new_name = update.message.text
    cud = context.user_data
    cud[name] = new_name
    update.message.reply_text(f'Hallo {cud[name]}! Du kannst mich Pya nennen! Was ist dein Lieblingsfach?')
    return SUBJECT

def subject(update, context):
    new_subject = update.message.text
    cud = context.user_data
    cud[subject] = new_subject
    if cud[subject].lower() == 'informatik':
        update.message.reply_text('Das ist ja ein Zufall! Ich mag informatik auch am liebsten! Ich wurde nämlich mit der Programmiersprache Python geschrieben!')
    elif cud[subject].lower() == 'sport':
        update.message.reply_text('Oh, für dafür bin ich immer viiiel zu faul.' )
    else:
        update.message.reply_text(f'Ah ja, {cud[subject]}! Das mag ich auch ganz gerne, aber mein Lieblingsfach ist Informatik!')
    update.message.reply_text('Und was ist dein Lieblingessen?')
    return FOOD

def food(update, context):
    new_food = update.message.text
    cud = context.user_data
    cud[food] = new_food
    if cud[food].lower() == 'pizza':
        update.message.reply_text('Ich liebe Pizza! Am liebsten mit ganz viel Käse!')
    else:
        update.message.reply_text(f'{cud[food]}, also. Das klingt auch sehr gut, aber noch lieber mag ich Pizza.')
    update.message.reply_text(f'Es war sehr interessant, ein bisschen mehr über dich zu erfahren. Ich glaube, ich mache jetzt erstmal einen Nap! Ich hoffe, wir sehen uns bald wieder, {cud[name]}!')
    return ConversationHandler.END

def memes(update, context):
    update.message.reply_text('Hier sind die besten Memes über alles mögliche!')
    reddit = praw.Reddit(client_id = 'P3pEG1jI2bWEwKImh3M5WQ',
                         client_secret = 'HhJd7ZG5VkV7N3OgQDBcK_Fz4mjg3g',
                         user_agent = 'meme-collector')

    subreddit = reddit.subreddit('ich_iel')
    posts = subreddit.hot(limit=10)

    image_urls = []
    image_titles = []
    image_scores = []
    image_timestamps = []
    image_ids = []

    for post in posts:
      image_urls.append(post.url.encode('utf-8'))
      image_titles.append(post.title.encode('utf-8'))
      image_scores.append(post.score)
      image_timestamps.append(datetime.datetime.fromtimestamp(post.created))
      image_ids.append(post.id)

    for i in image_urls:
        update.message.reply_text(f'{i}')

def main():
    updater = Updater("5123726634:AAG3mhhKYixp9t7eyGrwPs8WTnQQbGxe3UM",
                      use_context=True)
    dp = updater.dispatcher
    # conversation handler for 'real' conversations
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('chat', chat)],
        fallbacks=[],
        states={
            NAME: [MessageHandler(Filters.text, name)],
            SUBJECT: [MessageHandler(Filters.text, subject)],
            FOOD: [MessageHandler(Filters.text, food)]
            })
    dp.add_handler(conv_handler)
    # command handler for /commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('hallo', hallo))
    dp.add_handler(CommandHandler('memes', memes))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# some commands:
# update.message.reply_text('your message'): send a message
# update.message.text: get last sent message
# context.user_data[xy]: store parameters outside of a function
# send documents/plots/figures:
# chat_id = update.message.chat_id
# document = open('XY','rb')
# context.bot.send_document(chat_id, document)

