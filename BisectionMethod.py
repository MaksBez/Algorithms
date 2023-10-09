import math

def f(x):
    fnc = math.exp(-x) + x**2
    return fnc

def fx(x):
    fnc = -math.exp(-x) + 2*x
    return fnc

a_initial = -10
b_initial = 10
a_list = [a_initial]
b_list = [b_initial]
k = 0

while(b_list[k] - a_list[k]) >= 10**(-8):
    if fx((a_list[k] + b_list[k]) / 2) > 0:
        a_list.append(a_list[k])
        b_list.append((a_list[k] + b_list[k]) / 2)
    elif fx((a_list[k] + b_list[k]) / 2) < 0:
        a_list.append((a_list[k] + b_list[k]) / 2)
        b_list.append(b_list[k])
    solution_x = (b_list[k] + a_list[k]) / 2 
    k += 1

print("x* = ", solution_x)
print("f(x*) = ", f(solution_x))

