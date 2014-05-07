#! encoding: utf-8

import matplotlib.pyplot as pl

# Añadir leyendas 

# Lista con los valores de x e y de una función
x0 = [ 1, 2, 3, 4, 5]
y0 = [ 1, 4, 9, 16, 25]

# Lista con los valores de x e y de otra función
x1 = [ 1, 2, 4, 6, 8]
y1 = [ 2, 4, 8, 12, 16]

# Trazar ambas funiones
plot0 = pl.plot(x0,y0,'r--', label='cuadrado')
plot1 = pl.plot(x1,y1,'bo', label='doble')

# Incluir un título
pl.title('Dibujar x frente a y') 

# Poner etiquetas en los ejes 
pl.xlabel('Algunos enteros positivos')
pl.ylabel('Cuadrado y doble de algunos enteros')

# Poner limites a los ejes 
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.0)

# Poner una leyenda
#                   localizacion:
#  'best'               0
#  'upper right'        1
#  'upper left'         2
#  'lower left'         3
#  'lower right'        4
#  'right'              5
#  'center left'        6
#  'center right'       7
#  'lower center'       8
#  'upper center'       9
#  'center'             10

pl.legend(loc=2, numpoints=4) 
#pl.legend(['cuadrado', 'doble'], loc=2, numpoints=4) 

# mostrar por la consola el resultado
pl.show()
