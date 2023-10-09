import sympy as sym
import time

"""
Bisection Method for minimizing a 1-Dimensional Function
"""

# Setting x as the variable symbol
x = sym.symbols('x', real = True)

# Input desired Function here
def f():
    return sym.exp(-x) + x**2

# Plots the function
def plot_function():
    return sym.plot(f(), line_color = "red")

# Evaluates the function
def f_evaluate(x1):
    return f().subs({x: x1})

# Finds derivative of the function
def fx(x1):
    return sym.diff(f(), x).subs({x: x1})

# Bisection Method Algorithm
def BisectionMethod(initial_a, initial_b):

    # Set starting points
    a_current = initial_a
    b_current = initial_b
    iterations = 0

    # Loop runs until they are within 10**-8 of each other
    while(b_current - a_current) >= 10**(-8):
        # Case 1, derivative > 0 
        if fx((a_current + b_current) / 2) > 0:
            a_next = a_current
            b_next = (a_current + b_current) / 2
        
        # Case 2, derivative < 0 
        elif fx((a_current + b_current) / 2) < 0:
            a_next = (a_current + b_current) / 2
            b_next = (b_current)

        # Case 3, solution found return ((a_current + b_current) / 2)
        elif fx((a_current + b_current) / 2) == 0:
            output = [f"x* = {((a_current + b_current) / 2)}", f"f(x*) = {f_evaluate(((a_current + b_current) / 2))}"]
        
        # Update a and b
        a_current = a_next
        b_current = b_next

        iterations += 1
    # Final solution after while loop ends
    solution = (a_current + b_current) / 2 

    # Create output and return it
    output = [f"x* = {solution}", f"f(x*) = {f_evaluate(solution)}", f"Bisection Method Iterations = {iterations}"]
    return output

# Input two initial points, make sure they are not the same number
a_initial = -10
b_initial = 10

# Plot the desired function
plot_function()

# Runs the algorithm and times it
start_time = time.time()
print(BisectionMethod(a_initial, b_initial)[0], BisectionMethod(a_initial, b_initial)[1], BisectionMethod(a_initial, b_initial)[2])
end_time = time.time()
print(f"Bisection Method Run Time: {round(end_time - start_time, 10)}")



