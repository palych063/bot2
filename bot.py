import telebot
from telebot.types import Message   

TOKEN = '906017936:AAH7tQvlViCcKAkG5NjRUGM13E6OHO8f7Hs'
STICKER_ID = 'CAADAgADZgIAAlRPCAABIE8pCZrZTYIWBA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
    bot.reply_to(message, 'No answer')

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, str('Хуй'))

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)

bot.polling(timeout=60)
