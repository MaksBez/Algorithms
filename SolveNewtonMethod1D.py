import sympy as sym

"""
Newtons Method for solving functions f(x) = 0
"""

m = sym.symbols('m')

# Enter Desired Function here
def funct():
  return 7*m**4 + 3*m**3 + 2*m**2 + 9*m + 4 

# Evaluates f(x) at value y
def f(y):
  return funct().subs(m, y).evalf()

# Evaluates f'(x) at value y
def fx(y):
  dfx = sym.diff(funct(), m)
  return dfx.subs(m, y).evalf()

initial = 1
x = [initial]
x.append(x[0] - f(x[0])/fx(x[0]))

k = 0
error_num = 0.01

while abs(f(x[k+1]) - f(x[k])) >= error_num:
    x.append(x[k+1] - f(x[k+1])/fx(x[k+1]))
    k += 1

print(f"x_final = {round(x[k+1], 6)}, f(x_final) = {round(f(x[k+1]), 6)}")
