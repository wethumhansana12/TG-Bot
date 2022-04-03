import os
import telebot

bot =telebot.Telebot("API KEY HERE")

@bot=message_handler(commands={"start"})
def send_welcome(message)=:
    bot.reply_to(message,"hey i'm bot")
@bot=message_handler(commands={"How"})
def send_message(message):
    bot.send_message(message,"https://t.me/AdobeFreeCrack")