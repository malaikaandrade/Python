import telebot 

token = #poner token

miBot = telebot.TeleBot(token)

@miBot.message_handler(commands = ['start', 'help'])

def send_welcome(message):
	miBot.reply_to(message, "Hola soy tu Bot")



chat_id = #poner chat id
miBot.send_message(chat_id, "Hola :)")

file = open("perrito.png", "rb")
miBot.send_photo(chat_id, file)

doc = open("miorimerbot.py", "rb")
miBot.send_document(chat_id,doc)

latitud = 19.325824
longitud = -99.182353
miBot.send_location(chat_id, latitud, longitud)

#
#

miBot.polling()

