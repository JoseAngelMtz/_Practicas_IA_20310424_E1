# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:47:20 2023

@author: josea
"""

"capitulo 27"
x = 0
while x <= 15:
    print(x)
    x +=5

x = 0
while x >= -100:
    print(x)
    x -=20
    
x = 10
while x >= 0:
    print('El valor del bucle es:',x)
    x -=1
    
"capitulo 28"
x = 0

while x <= 30:
    
    if x == 4 or x ==6 or x ==10:
        x = str(x)
        print('Se saltó el valor ' + x + ' de x')
        x = int(x)
    elif x == 15:
        x = str(x)
        print('Se rompió la ejecución del bucle cuando x valía ' + x)
        x = int(x)
        break
    else:print('El valor del bucle es:',x)
    x +=1
        
"capitulo 29"
colores = ('rojo','azul','verde','amarillo')

for i in colores:
    print('El color es: ' + i + '.')
    
"capitulo 30"
for i in range(7,700,100):
    print(i)