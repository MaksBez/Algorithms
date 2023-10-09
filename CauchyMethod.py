import sympy as sym
import numpy as np
"""
Cauchy's Method of steepest descent
"""

x, y= sym.symbols('x y', real = True)

# Enter Desired Functions here
def funct():
  return 5*x**2 + 7*y**2 - 3*x*y

# Returns value of function
def f(x1,y1):
    return funct().subs({x: x1, y: y1})

# Returns Gradiant of a function
def gradf1(x_1, x_2):
    gradient = [(sym.diff(funct(), x)), (sym.diff(funct(), y))]
    return [gradient[0].subs({x: x_1 ,y: x_2}), gradient[1].subs({x: x_1 ,y: x_2})]

#  Magnitude of a vector
def magnitude(vector):
    total = 0
    for num in vector:
        total += num*num
    return sym.sqrt(total).evalf()
    
# Initialize
x_1 = [0, 1]
x_current = x_1
error_term = 10**-5
ITMAX = 0

while ( (magnitude(gradf1(x_current[0],x_current[1])) / (1+f(x_current[0],x_current[1]))) >= error_term) and (ITMAX < 1000):
    d_current = gradf1(x_current[0], x_current[1])
    lambda_current = 0.001
    d_curr = np.array([-d_current[0], -d_current[1]])
    x_next = x_current + d_curr * lambda_current
    x_current = x_next
    ITMAX += 1

print(f"Final X = {x_current}")