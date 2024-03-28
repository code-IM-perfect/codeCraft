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


###############################  ATTENDANCE  ###############################

def get_attendance(message,rollNo,backupMessage):
	dates = re.findall("\d\d",message.text)
	if len(dates)==6:
		months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		fromDate = f"{int(dates[0])}-{months[int(dates[1])-1]}-20{dates[2]}"
		toDate = f"{int(dates[3])}-{months[int(dates[4])-1]}-20{dates[5]}"
		bot.send_message(message.chat.id, f"Getting attendance for {rollNo}\nFrom {fromDate} to {toDate}")
		bot.send_message(message.chat.id, "http://172.26.192.62/Smartrollcall/Account/Login")
		bot.send_message(message.chat.id, f"http://172.26.192.62/Smartrollcall/Reports/ReportViewer.aspx?ReportID=11&Category=1&from={fromDate}&to={toDate}&RollNumber={rollNo}")
		bot.send_message(message.chat.id, "Open *BOTH* these links to see your attendance. The second link will not open unless the first one is already open\n\nAlso you need to be on the IITK network (iit wifi or vpn)")
	else:
		bot.send_message(message.chat.id, "Uhh something seems to be wrong with the date format")
		attendance_ask_date(backupMessage)
		return 0

	

def attendance_ask_date(message):
	rollNo = re.findall("\d\d\d\d\d\d\d\d|\d\d\d\d\d\d",message.text)

	if (not rollNo):
		bot.send_message(message.chat.id, "Uhh the RollNo seems to be wrong")
		attendance_ask_roll(message)
		return 0

	bot.send_message(message.chat.id,"Okay, from when to when?")
	askingStartDate = bot.send_message(message.chat.id,"Input format-\n`DD-MM-YY DD-MM-YY`\nlike `13-02-24 05-03-24`", parse_mode="markdown")
	bot.register_next_step_handler(askingStartDate, get_attendance, rollNo[0],message)

@bot.message_handler(commands=['attendance'])
def attendance_ask_roll(message):
	askingRoll = bot.send_message(message.chat.id, "So you're calculating if you can leave today's class?\nCool just gimme your *Roll No*", parse_mode="markdown")
	bot.register_next_step_handler(askingRoll, attendance_ask_date)



bot.infinity_polling()