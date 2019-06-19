import smtplib
import getpass

def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
	print("Preparando el correo....")
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)


	# pasos del protocolo SMTP
	smtpserver.ehlo() #Saludo al servidor
	smtpserver.starttls() #Agrega otra capa de seguridad

	try:
		smtpserver.login(remitente, password)
	except:
		print("No has configurado, favor de revisar")

	header = "To: {0}\nFrom: {1}\nSubject: {2}\n".format(destinatario, remitente, asunto)
	msg = header + "\n{0}\n\n".format(cuerpo)
	print(msg)


	smtpserver.sendmail(remitente, destinatario, msg)
	smtpserver.close()
	# si no cerramos los flujos, puede llegar a haber procesos que ocupen memoria interna y retrasar algunos procesos
	#es una buena practica siempre cerrar flujos
	#estos correos se van a comportar como jsons por lo que utilizamos los headers, los headers son las cabeceras que llevan metadaros, los datos se comportan como json y header , los headers llevan el from y el subject en este caso

if __name__ == "__main__":

	usuario = input("Escribe el remitente: ")
	password = getpass.getpass("Escriba su contraseña: ")
	destinatario = input("Escriba el destinatario: ")
	asunto = input("Escriba el asunto: ")
	cuerpo = input("Escriba su mensaje: ")

	enviar_correo(usuario, password, destinatario, asunto, cuerpo)