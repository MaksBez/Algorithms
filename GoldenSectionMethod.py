import math
def f(x):
    fnc = math.exp(-x) + x**2
    return fnc

a_initial = -100
b_initial = 100
r = (3 - (math.sqrt(5))) / 2
a_list = [a_initial]
b_list = [b_initial]
lambda_list = [a_list[0] + r*(b_list[0] - a_list[0])]
mu_list = [a_list[0] + (1-r)*(b_list[0] - a_list[0])]

k = 0
while ((b_list[k] - a_list[k]) >= 10**(-8)):
    if f(lambda_list[k]) > f(mu_list[k]):
        a_list.append(lambda_list[k])
        lambda_list.append(mu_list[k])
        b_list.append(b_list[k]) 
        mu_list.append(a_list[k+1] + (1-r)*(b_list[k+1] - a_list[k+1]))
    elif f(lambda_list[k]) < f(mu_list[k]):
        a_list.append(a_list[k])
        b_list.append(mu_list[k])
        mu_list.append(lambda_list[k])
        lambda_list.append(a_list[k+1] + r*(b_list[k+1] - a_list[k+1]))
    else:
        solution_x = (b_list[k] + a_list[k]) / 2
        break
    solution_x = (b_list[k] + a_list[k]) / 2
    k += 1

print("x* = ", solution_x)
print("f(x*) = ", f(solution_x))