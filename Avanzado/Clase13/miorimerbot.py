import telebot

token = '838885317:AAE9Zg3Wsb3Bl5kmg8x7INbIpsDstq0XRg8'

miBot = telebot.TeleBot(token)

#Recibe los mensajes que enviemos desde telegram.
def escucha(mensajes):
	for m in mensajes:
		#print(m)
		chat_id = m.chat.id
		miBot.send_message(chat_id,"Tu id es: "+str(chat_id))
		if m.content_type == 'text':
			text = m.text
			miBot.send_message(chat_id, "Enviaste el texto: "+text)


miBot.set_update_listener(escucha)
miBot.polling()

#Cuando reciba un mensaje te regresa tu id y el mensaje que le enviaste.import telebot
