import matplotlib.pyplot as pl

# Lista con los valores de x
x = [ 1, 2, 3, 4, 5]

# Lista con los valores de f(x)
y = [ 1, 4, 9, 16, 25]

# Utilizar la funcion plot para trazar el grafico 
# cambiar el estilo de la linea 
pl.plot(x,y,'--g')

# mostrar por la consola el resultado
pl.show()
