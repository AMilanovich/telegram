import telebot
import requests

bot = telebot.TeleBot('954668606:AAER9Kv9qxd841n2FJrcpF8fgJCRLQeyscU')
API = "http://api.openweathermap.org/data/2.5/weather?q=Minsk,blr&APPID=e876f3b4b56e27cfc2fa61e94bcf3fb2"

response = requests.get(API)
if response.ok:
    data = response.json()

print(data)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

    elif message.text == ("/w", "/What the wether like to day"):
        bot.send_message(message.from_user.id, data)
    else:
        bot.send_message(message.from_user.id, "Напиши /w or /What the wether like to day")


bot.polling(none_stop=True, interval=0)
