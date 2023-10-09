# %%
import sympy as sym
from sympy import *

# BFGS Method

x1, x2 = sym.symbols('x1 x2', real = True)

def f_gradient(fxy, point1, point2):
    f_1 = diff(fxy, x1).subs(x1, point1).subs(x2, point2)
    f_2 = diff(fxy, x2).subs(x1, point1).subs(x2, point2)
    return [f_1, f_2]

def magnitude(vector):
    total = 0
    for num in vector:
        total += num*num
    return sym.sqrt(total).evalf()

funct = x1**2 + 2*x2**2 - 2*x1*x2 - 2*x2

x0 = sym.Matrix([0, 0]) # Initial Guess

H0 = sym.Matrix.eye(2)
funct_gradient_x0 = sym.Matrix(f_gradient(funct, x0[0], x0[1]))

ITEMAX = 0
error = 10**-8

H_current = H0
x_current = x0
funct_gradient_current = funct_gradient_x0

print(f"Initial point: {x0}")
print(" ")
while (ITEMAX < 1000) and (magnitude(funct_gradient_current) / (1+(funct.subs(x1, x_current[0]).subs(x2, x_current[1]))) > error):
    funct_gradient_current = sym.Matrix(f_gradient(funct, x_current[0], x_current[1])) 

    d_current = -H_current*funct_gradient_current
    lambda_current_upper = d_current.T * funct_gradient_current
    lambda_current_lower = d_current.T * H_current * d_current
    lambda_current = -lambda_current_upper[0] / lambda_current_lower[0]

    x_next = x_current + lambda_current*d_current

    s_current = x_next - x_current

    funct_gradient_next = sym.Matrix(f_gradient(funct, x_next[0], x_next[1])) 

    y_current = funct_gradient_next - funct_gradient_current

    eq1_upper = s_current * s_current.T
    eq1_lower = s_current.T * s_current
    eq2_upper = H_current * y_current * y_current.T * H_current
    eq2_lower = y_current.T * H_current * y_current
    H_next = H_current + ((eq1_upper)/(eq1_lower[0])) - ((eq2_upper)/(eq2_lower[0]))
    
    x_current = x_next.evalf(4)
    H_current = H_next.evalf(4)
    d_current = d_current.evalf(4)
    print(f"Search Direction at k = {ITEMAX}: {d_current}")
    print(f"Step Length at k = {ITEMAX}: {lambda_current}")
    print(f"x at k = {ITEMAX + 1}: {x_next}")

    ITEMAX += 500
# %%
