import smtplib
import getpass

def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
	print("Preparando el correo....")
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)


	# pasos del protocolo SMTP
	smtpserver.ehlo() #Saludo al servidor
	smtpserver.smtpstarttls() #Agrega otra capa de seguridad

	try:
		smtpserver.login(remitente, password)
	except:
		print("No has configurado, favor de revisar")

	header = "To: {0}\nFrom: {1}\nSubject: {2}\n".format(destinatario, remitente, asunto)
	msg = header + "\n{0}\n\n".format(cuerpo)
	print(msg)


	smtpserver.sendmail(remitente, destinatario, msg)
	smtpserver.close()
	
