import sympy as sym

"""
Newtons Method for minimizing functions f(x1, x2)
"""

x, y= sym.symbols('x y', real = True)

# Enter Desired Functions here
def funct():
  return 2*x**2 + y**2 - 2*x*y+2*x**3+x**4

def f(x1,y1):
    return funct().subs({x: x1, y: y1})

def gradf1(x_1, x_2):
    gradient = [(sym.diff(funct(), x)), (sym.diff(funct(), y))]
    return [gradient[0].subs({x: x_1 ,y: x_2}), gradient[1].subs({x: x_1 ,y: x_2})]

#  Magnitude of a vector
def magnitude(vector):
    total = 0
    for num in vector:
        total += num*num
    return sym.sqrt(total).evalf()
    
x_0 = [0, -2]
d_0 = gradf1(x_0[0],x_0[1])
print(d_0)
lambda_0 = 0.0001
x_1 = x_0 + lambda_0*d_0
error_term = 10**-4

d_current = d_0
x_current = x_1
lambda_current = lambda_0
J_current = sym.Matrix([[1,0],
                        [0,1]])

while magnitude(x_1) >= error_term:
    d_current = -(J_current)*(sym.Matrix.transpose(J_current)) * gradf(x_current[0],x_current[1])
    x_next = x_current + lambda_current*d_current
    s_current = lambda_current*d_current
    y_current = gradf1(x_next[0],x_next[1]) - gradf1(x_current[0],x_current[1])

    # Choose v_current
    
    
    # Choose J_next

