import sqlite3
conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cliente(cliente_id integer PRIMARY KEY AUTOINCREMENT, nombre varchar(30), edad integer, curp varchar(18))")
cursor.execute("CREATE TABLE IF NOT EXISTS tarjeta(tarjeta_id integer PRIMARY KEY AUTOINCREMENT, numero varchar(16) UNIQUE, clave varchar(4), fecha_vencimiento DATE, cliente_id INTEGER references cliente(cliente_id))")

bandera = True
while bandera:
	try:
		print("Selecciona una opción")
		print("\t1.-Insertar un cliente")
		print("\t2.-Insertar una tarjeta")
		print("\t3.-Consultar un cliente")
		print("\t4.-Actualizar un cliente")
		print("\t5.-Borrar un cliente")
		print("\t6.-Salir")



#PRIMARY KEY-- nos sirve para llamar de forma unica cada dato.   identifica de forma unica nuestros datos , como folio o como ID
#FOREIN KEY --identifica como unica  la tabla, y sirve para mandar a llamar tablas
conexion.commit()
conexion.close()