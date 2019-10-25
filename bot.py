import requests
import telebot
from telebot.types import Message

TOKEN = '906017936:AAH7tQvlViCcKAkG5NjRUGM13E6OHO8f7Hs'
STICKER_ID = 'CAADAgADZgIAAlRPCAABIE8pCZrZTYIWBA'
APP_ID = '5eb70066fb35a36dbb2361c8c3beedbb'

bot = telebot.TeleBot(TOKEN)
requests.get(f'https://api.telegram.org/bot{TOKEN}/deleteWebhook')


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    print(message)
    bot.reply_to(message, 'Иди пожалуйста нахуй ' +
                 message.from_user.first_name)


@bot.message_handler(commands=['погода'])
def send_weather(message: Message):
    if message.text[:7] == "Погода " or message.text[:7] == "погода ":
        try:
            city = message.text[7:]
            r = requests.get('http://api.openweathermap.org/data/2.5/weather',
                             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': APP_ID})
            data = r.json()
            bot.send_message(message.chat.id, "Температура в {}: {} C, от {} до {}".format(
                city,
                data['main']['temp'],
                data['main']['temp_min'],
                data['main']['temp_max']))
        except Exception as e:
            bot.send_message(message.chat.id, data['message'])
            pass


@bot.message_handler(content_types=['text'])
def handle_t(message: Message):
    print(message)
    if message.text[:7] == "Погода " or message.text[:7] == "погода ":
        try:
            city = message.text[7:]
            r = requests.get('http://api.openweathermap.org/data/2.5/weather',
                             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': APP_ID})
            data = r.json()
            bot.send_message(message.chat.id, "Температура в {}: {} C, от {}C до {}C".format(
                city,
                data['main']['temp'],
                data['main']['temp_min'],
                data['main']['temp_max']))
        except Exception as e:
            bot.send_message(message.chat.id, data['message'])
            pass


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


bot.polling(timeout=60)
