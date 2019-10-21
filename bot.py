import requests
import telebot
from telebot.types import Message   

TOKEN = '906017936:AAH7tQvlViCcKAkG5NjRUGM13E6OHO8f7Hs'
STICKER_ID = 'CAADAgADZgIAAlRPCAABIE8pCZrZTYIWBA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
    bot.reply_to(message, 'No answer')

@bot.message_handler(content_types=['text'])
def handle_t(message: Message):
    if message.text[:7] == "Погода " or message.text[:7] == "погода ":
            city = message.text[7:]
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?&units=metric&q=%s&appid=0c9f3c052f1d81b7062750ff0926f345<img src="https://habrastorage.org/files/8fa/5f5/313/8fa5f5313b37438eb250b22cf041f2dd.png" alt="image"/>' % (city))
            data = r.json()
            temp = data["main"]["temp"]            
            bot.send_message(message.chat.id, "Температура в {}: {} C".format(city, temp))

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


bot.polling(timeout=60)