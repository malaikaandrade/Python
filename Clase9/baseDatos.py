"""
una base de satos es un almacen que nos permite guardar grandes cantidades de imformacion de forma organizada para que la podamos encontrar y utilizar facilmente

una base de datos se compone de:
-entidades: cualquier objeto o concepto sobre el que se recoge informacion: cosa, persona, concepto abstracto o suceso. ej: profesor materia.
existen dos tipos de entidades:
-fuertes: la existencia no depende de la existencia de otra.
-debiles: su existencia depende de la existencia de otra entidad.


-atributos: son caracteristicas de interes sobre una identidad.
existen de tipo:
-monovaluado: se refiere a un solo valor
-multivaluado: representa varios valores

-relaciones, cardinalidad: es una correspondencia o asociacion entre dos o mas entidades
-cardinalidad: especifica el numero minimo y numero max de correspondencias en las que puede tomar parte cada ocurrencia.

relaciones---aciones(normalmente)

(1,1) uno a uno
(1-n) uno a muchos
(1-n) muchos a uno
(n-n) muchos a muchos


-claves

hay muchos tipos de modelado de base de datos
el modelo es la representacion de la realidad que conserva solo los detalles relevantes para modelar la base de dafos quwe se requiere:
-modelo conceptual
-modelo logico
-modelo fisico



modelo conceptual -refleja tan solo la existencia de los datos, independiente del sistema gestor de la base de datos.

se lee desde la entidad hacia la relacion

diagrama

				  1N
profesor--------enseña---------alumno
(1,1)							(0,	n)


Un profesor enseña a ninguno o muchos alumnos y un alumno tiene exactamente un tutor

modelo logico: estre modelo sirve para cualquier tipo de SGBD

MODELO FISICO: se transforman las entidades en tablas, las instancias en filas y los atributos en columnas

funciones basicas de una base de datos
C reate 
R ead
U pdate
D elete
"""

