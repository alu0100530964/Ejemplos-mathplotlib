#!encoding: utf-8

import matplotlib.pyplot as pl

# Mostrar más de una representación en el mismo lienzo 

diagrama1 = pl.figure(1)

# la figura tendra 2 filas y 1 columna y se quiere trazar en la primera
pl.subplot(421)

# para trazar en la segunda 
pl.subplot(428)

# mostrar por la consola el resultado
pl.show()
