from tkinter import *
ventana = Tk()
ventana.title("Cuestionario de la pareja ideal")
ventana.geometry("500x500")

def eleccion():
	if opcion.get()==1:
		mensaje.set("Apto para un sugar, good girl!")
	elif opcion.get()==2:
		mensaje.set("Tienes muy buenos gustos.")

	elif opcion.get()==3:
		mensaje.set("Que bueno que pienses en eso.")

	elif opcion.get()==4:
		mensaje.set("Siempre hay que pensar en la comida.")

	elif opcion.get()==5:
		mensaje.set("Nunca te vas a aburrir y siempre vas a conocer nuevos lugares.")
		# el set es un metodo que sirve para mostrar los mensaje sen pantalla

#recuperar la opcion seleccionada por el usuario 
opcion = IntVar()
#mensaje mostrado en pantalla
mensaje = StringVar()
#decorando pantalla
etiqueta1 = Label(ventana, text="¿Qué ves en el/ella?").place(x=20, y=40)
etiqueta2 = Label(ventana, textvariable=mensaje).place(x=20, y=230)

op1 = Radiobutton(ventana, text="Tiene dinero", value=1, variable=opcion).place(x=20, y=60)
op2 = Radiobutton(ventana, text="Es científico", value=2, variable=opcion).place(x=20, y=80)
op3 = Radiobutton(ventana, text="Tiene bonitos sentimientos", value=3, variable=opcion).place(x=20, y=100)
op4 = Radiobutton(ventana, text="Tiene buen apetito", value=4, variable=opcion).place(x=20, y=120)
op5 = Radiobutton(ventana, text="Le gusta salir a pasear", value=5, variable=opcion).place(x=140, y=60)

boton = Button(ventana, text="Intentar", command=eleccion).place(x=20, y=190)



ventana.mainloop()