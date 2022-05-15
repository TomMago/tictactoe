from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import praw
import urllib
import pandas as pd
import datetime

from board import Board
from engine import Engine

# get API token from BotFather on telegram
# define commands/conversation line like:

# defining conversation states
TURN = 1

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
    reddit = praw.Reddit(client_id = 'client id',
                         client_secret = 'client secret',
                         user_agent = 'user agent')

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

def tictactoe(update, context):
    context.user_data[0] = Board()
    context.user_data[1] = 2 # use_engine 0: no engine, 1: engine player one, 2: engine player two
    context.user_data[2] = Engine(context.user_data[1]) # engine


    if context.user_data[0].to_move == context.user_data[1]:
        update.message.reply_text(context.user_data[0].text_board())
        update.message.reply_text("Engine calculating...")
        context.user_data[2].negamax(context.user_data[0],True, 1)
        coordinates = tuple(context.user_data[2].best_move)
        context.user_data[0].make_move(context.user_data[0].to_move, (coordinates[0], coordinates[1]))

    update.message.reply_text(context.user_data[0].text_board())
    update.message.reply_text("Enter move: ")
    return TURN

def turn(update, context):
    cords = update.message.text
    coordinates = np.array(cords.split()).astype(np.int64)
    context.user_data[0].make_move(context.user_data[0].to_move, (coordinates[0], coordinates[1]))

    update.message.reply_text(context.user_data[0].text_board())

    if context.user_data[0].check_win():
        if context.user_data[0].check_win() == 1:
            update.message.reply_text("Player 1 wins!")
        elif context.user_data[0].check_win() == 2:
            update.message.reply_text("Player 2 wins!")
        elif context.user_data[0].check_win() == 3:
            update.message.reply_text("Draw!")
        return ConversationHandler.END

    update.message.reply_text("Engine calculating...")
    context.user_data[2].negamax(context.user_data[0],True, 1)
    coordinates = tuple(context.user_data[2].best_move)
    context.user_data[0].make_move(context.user_data[0].to_move, (coordinates[0], coordinates[1]))

    if context.user_data[0].check_win():
        if context.user_data[0].check_win() == 1:
            update.message.reply_text("Player 1 wins!")
        elif context.user_data[0].check_win() == 2:
            update.message.reply_text("Player 2 wins!")
        elif context.user_data[0].check_win() == 3:
            update.message.reply_text("Draw!")
        return ConversationHandler.END

    update.message.reply_text(context.user_data[0].text_board())
    update.message.reply_text("Enter move: ")

    return TURN


def main():
    updater = Updater("5249417340:AAHa7InAmLUcP5Z5GuXH6-7W9u1AEkpYAsY",
                      use_context=True)
    dp = updater.dispatcher
    # conversation handler for 'real' conversations
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('tictactoe', tictactoe)],
        fallbacks=[],
        states={
            TURN: [MessageHandler(Filters.text, turn)],
#            FINISH: [MessageHandler(Filters.text, finish)]
            })
    dp.add_handler(conv_handler)
    # command handler for /commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('hallo', hallo))
    dp.add_handler(CommandHandler('memes', memes))
    dp.add_handler(CommandHandler('tictactoe', tictactoe))
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

