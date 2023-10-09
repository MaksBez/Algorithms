import sympy as sym

"""
Newtons Method for solving functions f1(x1, x2) = 0, f2(x1,x2) = 0
"""

x1, x2 = sym.symbols('x1 x2', real = True)

# Enter Desired Functions here
def funct1():
  return 3*x1*x2 + 7*x1 + 2*x2 - 3
def funct2():
  return 5*x1*x2 - 9*x1 - 4*x2 + 6

def f1(x_1,x_2):
    return funct1().subs({x1: x_1, x2: x_2})
def f2(x_1,x_2):
    return funct2().subs({x1: x_1, x2: x_2})

# Find the gradient
def gradf1(x_1, x_2):
    gradient = [(sym.diff(funct1(), x1)), (sym.diff(funct1(), x2))]
    return [gradient[0].subs({x1: x_1 ,x2: x_2}), gradient[1].subs({x1: x_1 ,x2: x_2})]

def gradf2(x_1, x_2):
    gradient = [(sym.diff(funct2(), x1)), (sym.diff(funct2(), x2))]
    return [gradient[0].subs({x1: x_1 ,x2: x_2}), gradient[1].subs({x1: x_1 ,x2: x_2})]

#  Magnitude of a vector
def magnitude(vector):
    total = 0
    for num in vector:
        total += num*num
    return sym.sqrt(total).evalf()

# Initialization
initialx1 = 1
initialx2 = 1
x1x2 = [initialx1, initialx2]
error_num = 0.00001
difference = sym.Matrix( [9999, 9999] ) # for the loop

# Runs the Newtons Algorithm
while magnitude(difference) >= error_num:
    matrix_solutions = sym.Matrix( [x1x2[0], x1x2[1]] )

    invArray = sym.Matrix([ [gradf1(x1x2[0], x1x2[1])[0], gradf1(x1x2[0], x1x2[1])[1]],
                        [gradf2(x1x2[0], x1x2[1])[0], gradf2(x1x2[0], x1x2[1])[1]] ])

    NormArray = sym.Matrix([[f1(x1x2[0], x1x2[1]),  
                         f2(x1x2[0], x1x2[1])] ])

    next_x = (matrix_solutions - (invArray.inv() * NormArray.transpose()))

    previousx1x2 = [x1x2[0], x1x2[1]]
    x1x2[0] = next_x[0]
    x1x2[1] = next_x[1]

    matrix_previous = sym.Matrix( [f1(previousx1x2[0], previousx1x2[1]), 
                               f2(previousx1x2[0], previousx1x2[1])] )
    matrix_current = sym.Matrix([f1(x1x2[0], x1x2[1]), 
                                f2(x1x2[0], x1x2[1])] )
    difference = abs(matrix_previous - matrix_current)

print(f"x_1 = {round(x1x2[0].evalf(),5)}, x_2 = {round(x1x2[1].evalf(), 5)}")
print(f"f1(x1, x2) = {round(f1(x1x2[0], x1x2[1]).evalf(), 4)}, f2(x1,x2) = {round(f2(x1x2[0], x1x2[1]).evalf(),4)}")