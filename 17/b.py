import sympy as sp
from sympy import cos
n, z, u, w = sp.symbols('n z u w')
x_n = cos(w*n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(w*n) u[n]:")
sp.pprint(X_z, use_unicode=True)

