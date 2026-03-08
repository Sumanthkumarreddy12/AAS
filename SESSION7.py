import sympy as sp

# define variable
x = sp.symbols('x')

# define function
f = (x - 3)**2

# compute derivative
derivative = sp.diff(f, x)

# solve derivative = 0
minima = sp.solve(derivative, x)

print("Function:", f)
print("Derivative:", derivative)
print("Minimum point x =", minima[0])
OUTPUT:
Function: (x - 3)**2
Derivative: 2*x - 6
Minimum point x = 3
