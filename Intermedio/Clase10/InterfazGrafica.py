"""
INTERFAZ GRAFICA

"""
from tkinter import *
# cuando queramos importarlo toda la libreria -----import tkinter as tk
ventana = Tk()
#para darle las dimensiones a la ventana
#las unidades de medida de las ventanas son pixeles (ancho por altura)

def quitar():
	ventana.destroy()

ventana.geometry("600x600")
boton = Button(ventana, text="Cómeme", bg="pink", fg="light blue")
#ponemos la ubicacion de nuestro boton sobre la ventana
boton.place(x=250, y=250, width=180, height=65)

boton2 = Button(ventana, text="S A L I R", command=quitar)
boton2.place(x=20, y=70, width=180, height=65)







ventana.mainloop()

