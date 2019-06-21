from tkinter import *
ventana = Tk()
ventana.geometry("1000x600")
img = PhotoImage(file = "giphy.gif")
widget = Label(ventana, image=img).pack()



ventana.mainloop()
