import math
def f(x):
    fnc = math.exp(-x) + x**2
    return fnc

def fx(x):
    fnc = -math.exp(-x) + 2*x
    return fnc

def Fibonacci_length(a, b, wid):
    n = 0
    Fib = [1, 1]
    while ((b-a)/wid) >= Fib[n]:
        v = Fib[n]
        v_next = Fib[n+1]
        added = v + v_next
        Fib.append(added)
        n += 1
    return n

def Fibonacci_List(howlong):
    Fib_list = [1, 1]
    for i in range(0, howlong):
        a = Fib_list[i]
        b = Fib_list[i+1]
        c = a + b
        Fib_list.append(c)
    return Fib_list

a_initial = -10
b_initial = 10

error = 10**(-8)

n_final = Fibonacci_length(a_initial, b_initial, error) - 1
Final_Fib_List = Fibonacci_List(n_final)

a_list = [0] * n_final
b_list = [0] * n_final
lambda_list = [0] * n_final
mu_list = [0] * n_final

a_list[0] = a_initial
b_list[0] = b_initial
lambda_list[0] = a_list[0] + ((Final_Fib_List[n_final - 1 - 1])/(Final_Fib_List[n_final - 1 + 1]))*(b_list[0] - a_list[0])
mu_list[0] = a_list[0] + ((Final_Fib_List[n_final - 1])/(Final_Fib_List[n_final - 1 + 1]))*(b_list[0] - a_list[0])

for i in range(0, n_final - 1):
    if f(lambda_list[i]) > f(mu_list[i]):
        a_list[i + 1] = lambda_list[i]
        lambda_list[i + 1] = mu_list[i]
        b_list[i + 1] = b_list[i]
        mu_list[i + 1] = a_list[i + 1] + ((Final_Fib_List[n_final - (i + 1)])/(Final_Fib_List[n_final - (i + 1) + 1]))*(b_list[i+1] - a_list[i+1])
    elif f(lambda_list[i]) < f(mu_list[i]):
        a_list[i + 1] = a_list[i]
        b_list[i + 1] = mu_list[i]
        mu_list[i + 1] = lambda_list[i]
        lambda_list[i + 1] = a_list[i + 1] + ((Final_Fib_List[n_final - (i+1) - 1])/(Final_Fib_List[n_final - (i+1) + 1]))*(b_list[i+1] - a_list[i+1])
    solution_x = (b_list[i-1] + a_list[i-1]) / 2

print("x* = ", solution_x)
print("f(x*) = ", f(solution_x))
