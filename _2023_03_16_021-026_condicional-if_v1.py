# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:35:05 2023

@author: josea
"""

"capitulo 21"
num1 = 15
num2 = 20

if num1 < num2:
	print('Se ejecuta el if.')

num1 = 1450
num2 = 60

if num1 > num2:
	print('Se ejecuta el if.')
    
num1 = 60
num2 = 60

if num1 != num2:
	print('Se ejecuta el if.')
    
"capitulo 22"
color = "rojo"

if color == "rojo":
    print("El color es rojo.")
else: 
    print("El color no es rojo.")
    
"capítulo 23"
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres sujeto a  credito.')
elif edad >= 45 and edad <= 100:
	print('Eres mayor de edad y ya1 no te contratan.')
elif edad >= 100 and edad <= 120:
	print('ya te vas a morir.')
else:
	print('Edad no válida.')
    
"capitulo 24"
colores = ('azul','rojo','amarillo','negro')
entrada = input('Ingrese el color a buscar\n')
if entrada in colores:
    if entrada in colores[0]:
        print('El color azul está admitido')
    elif entrada in colores[1]:
        print('El color rojo está admitido')
    elif entrada in colores[2]:
        print('El color amarillo está admitido')
    elif entrada in colores[3]:
        print('El color negro está admitido')
else:
    print('Color no admitido')

