#!/usr/lib/python3
# -*-coding:utf-8 -*-


import telebot

bot = telebot.TeleBot('954668606:AAER9Kv9qxd841n2FJrcpF8fgJCRLQeyscU')



http://api.openweathermap.org/data/2.5/weather?q=Minsk,blr&APPID=e876f3b4b56e27cfc2fa61e94bcf3fb2


class skoda_bot:

    @bot.message_handler(content_types=['text'])

    def get_text_messages(message):
        if message.text == "Skoda":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

