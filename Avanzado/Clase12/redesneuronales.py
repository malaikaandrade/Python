#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:33:05 2019

@author: malaikaandrade
"""
"""
REDES NEURONALES 
no le importa que sea la clasificacion optima, si no que llegue al resultado correcto
PERCEPTRON
 DOS ENTRADAS :     las entradas son las caracteristicas 
     input 0 --weight
                         output(una salida, resultado de la iteracion) generalmente la salida es la etiqueta

     input 1 --weight(que tanta importancia le estamos dando a una entrada u otra)

el weight nos ayuda a ir acomodando la recta de acuerdo a lo que has aprendido (se va modificando)

las wntradas se van a multiplicar con los pesos y van a pasar a una FUNCION DE ACTIVACION(NOS VA A DECIR SI SE REFIERE A UNA CLASIFICACION U OTRA, dependiendo de los pesos y las entradas)

BIAS- es un umbral que nos va a ayudar a que aunque nuestra entrada sea de 0 nos va a devolver un resultado de manera aleatoria, y estos valores se van ajustando a sus necesidades

MODELO MATEMATICO DE LA FUNCION DE ACTIVACIÓN

n
Ewixi + b(BIAS)
i=0

FUNCION SIGMOIDE- PROBABILIDAD DE QUE SEA UN VALOR U OTRO

******************** CALCULO DE ERRORES ***********************

            sigma = D - Y
            
        D = valor deseado
        Y = valor obtenido
        n = coeficiente de aprendisaje (que tan rapido aprende o que tanto quieres que aprenda)
            

"""
