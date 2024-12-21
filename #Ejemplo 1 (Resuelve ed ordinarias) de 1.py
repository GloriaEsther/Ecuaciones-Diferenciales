#Ejemplo 1 (Resuelve ed ordinarias) de 1er y 2do orden
from sympy import*
init_printing()
x= symbols("x")
y=Function("y")
y(x).diff(x,2)#en pantalla .diff muestra la derivada de una expresion en especifico

