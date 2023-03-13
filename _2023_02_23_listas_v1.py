# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:30:56 2023

@author: josea
"""

"capitulo 10"
print("pregunta 23, respuesta=amarillo")
print("pregunta 24, respuesta= rojo esta en la posicion 0 y el rosa en la posicion 7")
numeros=["tres","dos","cinco","cuatro","uno"]
print(numeros)

"capitulo 11"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("posicion -1=",colores[-1],"\nposicion -7=",colores[-7],"\nposicion -5=",colores[-5],"\nposicion -2=",colores[-2],"\nposicion -10=",colores[-10])

"capitulo 12"
del colores[-3]
del colores[1]
del colores[3]
del colores[4]
print(colores)

"capitulo 13"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.remove('amarillo')
colores.remove('rojo')
print(colores)

"capitulo 14"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colralma=[' ',' ']
colralma[0]=colores.pop(1)
colralma[1]=colores.pop(-2)
print(colralma)
print(colores)
"capitulo 15"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append('fuxia')
colores.append('celeste')
print(colores)

"capitulo 16"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-1,'turquesa')
colores.insert(-5,'magenta')
print(colores)

"capitulo 17"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.sort(reverse=True)
print(colores)

"capitulo 18"
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
cantidad= len(colores)
print(cantidad)
