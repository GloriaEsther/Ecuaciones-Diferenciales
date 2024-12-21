#matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import sympy
#from sympy import* 
from scipy import integrate
#init_printing()
# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')

# Resolviendo ecuación diferencial
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')



# definiendo la ecuación
eq = 1.0/2 * (y(x)**2 - 1)

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
edo_sol

C_eq = sympy.Eq(edo_sol.lhs.subs(x, 0).subs(ics), edo_sol.rhs.subs(x, 0))
C_eq

sympy.solve(C_eq)