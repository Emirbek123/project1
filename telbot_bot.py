import telebot 
import logging 
import datetime 
from telebot import types 
import requests  
from config import token

TOKEN = token
logging.basicConfig(filename='loc_bot.log', level=logging.INFO) 
bot = telebot.TeleBot(TOKEN) 



main_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
button1 = types.KeyboardButton(text='/start')


if __name__ == '__main__': 
    print('Bot is running!') 
    bot.polling()