#!/usr/bin/python

import telebot
import re

from bot_token import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message,"""
	Welcome! This is an iitk helper bot, it can do various things-
	- /start and /help : Show this message
	- /attendance : Get your attendance
	- /icardphoto : Get anybody's original student search photo
	- /customdp : Get anybody's Custom DP on student search
	- /motivate : Get a motivational quote
	""")

# @bot.message_handler(func=lambda m: m.text == "yooo")
# def echo_all(message):
# 	bot.reply_to(message, message.text)

def attendance_ask_starting_date(message):
	rollNo = re.findall("\d\d\d\d\d\d\d\d|\d\d\d\d\d\d",message.text)

	if (not rollNo):
		bot.send_message(message.chat.id, "Uhh the RollNo seems to be wrong")
		attendance_ask_roll(message)
		bot.send_message(message.chat.id, "fucking finally")
		
	
	askingStartDate = bot.send_message(message.chat.id,f"your roll no is {rollNo[0]}")

@bot.message_handler(commands=['attendance'])
def attendance_ask_roll(message):
	askingPass = bot.send_message(message.chat.id, "So you're calculating if you can leave today's class? Cool just gimme your *Roll No*", parse_mode="markdown")
	bot.register_next_step_handler(askingPass, attendance_ask_starting_date)

bot.infinity_polling()