archivo = open("ejemplo.txt", "r")

print(type(archivo))
print(archivo.read())

#todos los archivos .py son de texto plano 

#con este puedes crear archivos y escribir en el archivo
archivo_salida = open("prueba_salida.txt", "w")
archivo_salida.write("Esta es una prueba de escritura de archivo.")
archivo_salida.close()
#aqui cerramos el flujo

archivo_salida = open("prueba_salida.txt", "w")
archivo_salida.write("Esta es una prueba de escritura de archivo dos.")
#lo volvemos a abrir y escribimos sobre el 

