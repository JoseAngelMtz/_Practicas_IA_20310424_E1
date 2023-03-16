# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:52:39 2023

@author: josea
"""

"capitulo 34"
def sumas(num1,num2):
    suma=num1+num2
    print('el resultado de la suma es:',suma)
for i in range(3):
    sumas(int(input('ingrese el numero a sumar\n')),int(input('ingrese el 2° numero a sumar\n')))
    
"capitulo 35"
def colores(*args):
    print(len(args))
	

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

def colores2(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores2('azul','naranja')

def sumas2(*args):
    sumas=args[0]+args[1]+args[2]+args[3]+args[4]
    print('el resultado de la suma de los 5 nuemros es:',sumas)
    
sumas2(10,85,-9,4,17)