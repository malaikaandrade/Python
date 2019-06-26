import telebot
from telebot import types
import time

token = '838885317:AAE9Zg3Wsb3Bl5kmg8x7INbIpsDstq0XRg8'

miBot = telebot.TeleBot(token)

chat_id = 808142045


"""
while True: 
	hora = time.strftime("%X")
	#traeme la hora en formato de cadena y el formato en el que quieres que te la entregue
	if hora == "09:24:30": 
		miBot.send_message(chat_id, "!Ya despiertateeeeee!")
		break
"""

@miBot.message_handler(commands=["hora"])
def enviarHora(message):
	mensaje = "La hora actual es: "+time.strftime("%X")
	miBot.send_message(chat_id,mensaje)




markup = types.ReplyKeyboardMarkup(row_width=2)
item1 = types.KeyboardButton('/hora')
markup.add(item1)


miBot.send_message(chat_id, "Elige una opcion ", reply_markup=markup)
miBot.polling()