import tkinter as tk
ventana = tk.Tk()
ventana.title("Botones")
ventana.geometry("1000x600")

boton1 = tk.Button(ventana, text="Hola").grid(row=0, column=0)
boton2 = tk.Button(ventana, text="¿Cómo éstas?").grid(row=0, column=1)
boton3 = tk.Button(ventana, text="Piccola porzione").grid(row=0, column=1)
boton4 = tk.Button(ventana, text="Boton3", font=("Arial, 11")).grid(row=0, column=2)
boton5 = tk.Button(ventana, text="Cómeme").grid(row=1, column=0)
boton6 = tk.Button(ventana, text="Presióname").grid(row=1, column=1)
boton7 = tk.Button(ventana, text="Abrázame").grid(row=1, column=2)
boton8 = tk.Button(ventana, text="Quiéreme").grid(row=1, column=3)
boton9 = tk.Button(ventana, text="Boton").grid(row=2, column=0)
boton10 = tk.Button(ventana, text="Boton").grid(row=2, column=1)
boton12= tk.Button(ventana, text="Boton").grid(row=2, column=2)
boton13 = tk.Button(ventana, text="Boton").grid(row=2, column=3)

ventana.mainloop()