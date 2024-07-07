# !!! ADD THE BOT TO THE CHANNEL ADMINISTRATORS ON THE CHANNEL WHERE THE BOT CHECKS USERS !!!

import telebot
from telebot import types

api_token = 'Paste here your API-token from @BotFather'
channel = 'Paste here your channel username'
file_name = 'Paste here your file name (Example: file.txt)'

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_subscribe = types.InlineKeyboardButton(text='Subscribe✅', url=f'tg://resolve?domain={channel}')
    btn_check = types.InlineKeyboardButton(text='Check subscribe🔄', callback_data='check_subscribe')
    markup.add(btn_subscribe, btn_check)
    bot.send_message(message.chat.id, "Subscribe to the channel before get the file", reply_markup=markup) #message with buttons to user if they say '/start' command to bot and they not be subscribed to channel yet

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check_subscribe":
        user_status = bot.get_chat_member(channel, call.from_user.id).status
        if user_status in ['member', 'administrator', 'creator']:
            bot.send_message(call.message.chat.id, "✅Thanks for subscribe!")
            bot.send_document(call.message.chat.id, open(file_name, 'rb'))
        else:
            bot.send_message(call.message.chat.id, "❌You are not subscribe to the channel. Subscribe to the channel to get the file.") #message to user if they tap to 'Check subscribe🔄' button but not be subscribed to channel 

bot.polling()
