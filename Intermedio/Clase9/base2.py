import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()


alumnos = [('Derek', 21, 1232233, 6), ('Adri', 19, 23456, 10), ('Malaika', 19, 23456, 10)]
cursor.executemany("INSERT INTO alumno VALUES(?,?,?,?)", alumnos)
# los ? funcionan como comodines(cualquier tipo de variable) con lo que puedes rellenar la tabla
cursor.execute("SELECT * FROM alumno")
alumnitos = cursor.fetchall()
print(alumnitos)

#cambiando el nombre de la tabla
#renombrar = "ALTER TABLE alumno RENAME TO student"
#cursor.execute(renombrar)

conexion.commit()
conexion.close()