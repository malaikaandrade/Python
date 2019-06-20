import sqlite3

conexion = sqlite3.connect("ejemplo.db")
#todas las bases de datos las vamos a pasar a un archivo de tipo db(data base)
cursor = conexion.cursor()

#nos va a ejecutar 
#varchar--tipo de dato de base de datos, el numero indica el numero max de caracteres
#integer- numero de datos
try:
	cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<=10))")#atributos

except sqlite3.OperationalError:
	print("valio")

finally:
	cursor.execute("INSERT INTO alumno VALUES('Malaika', 20, 313015850, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Alejandra', 20, 313015895, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Brenda', 20, 313015840, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Abril', 20, 313016890, 10)")

#Recuperando contenido de las tablas
cursor.execute("SELECT * FROM alumno")
alumno = cursor.fetchone()
#te devuelve el registro que tenga enfrente(osea donde esta posicionado el cursor)
print(alumno)
alumnos = cursor.fetchmany(3)
print(alumnos)
conexion.commit()
conexion.close()


