# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:39:14 2023

@author: josea
"""

"capitulo 31"
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print('el modelo' , teclado2['Modelo'] ,'cuesta',teclado2['Precio'], '$')

"capitulo 32"
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
for i in teclado1:
     print(i,"=",teclado1[i]+".")
    
"capitulo 33"
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2)