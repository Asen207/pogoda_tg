import pyowm
import telebot

owm = pyowm.OWM('c02420713e9d8859ba5582939bb4c354',language="ru")
bot = telebot.TeleBot("708027929:AAGYPnKQB4y5TL8MZmHHb1OQ_xjsI8fGrSc")

@bot.message_handler(content_types=['text'])
def send_echo(message):#что принимет бот(пока не точно)
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp=w.get_temperature('celsius')['temp']
	#bot.reply_to(message, message.text)
	otwet ='В городе '+ message.text +w.get_detailed_status()+"\n"
	otwet +='Температура сейчас ' +str(temp)+"\n\n"
	bot.send_message(message.chat.id, otwet)
bot.polling( none_stop = True )