import sympy as sym
"""
Newtons Method for minimizing functions
"""
m = sym.symbols('m')

# Enter Desired Function here
def funct():
  return sym.log(sym.exp(m) + sym.exp(-m)) 

# Evaluates f(x) at value y
def f(y):
  return funct().subs(m, y).evalf()

# Evaluates f'(x) at value y
def fx(y):
  dfx = sym.diff(funct(), m)
  return dfx.subs(m, y).evalf()

# Evaluates f''(x) at value y
def fxx(y):
  d2fx = sym.diff(funct(), m, 2)
  return d2fx.subs(m, y).evalf()

# Finds appropriate lambda
def lambdatest(lmbda,xk1,xk2, a, b):
  fnc1 = xk1 + lmbda*(xk2-xk1)
  fnc2 = f(xk1+lmbda*(xk2 - xk1))
  final_list = [0,0]

  if a <= fnc1 <= b and fnc2 < f(xk1):
    final_list[0] = lmbda
    final_list[1] = 1
  else:
    final_list[0] = lmbda - 0.001
    final_list[1] = 0

  return final_list

# Finds appropriate i
def itest(i, xk1, deltak):
  testfnc = xk1 - (2^(-i))*(fx(xk1)) + (deltak)*(2^(-i/2))
  final_list = [i,0]

  if a <= testfnc <= b:
    final_list[0] = i
    final_list[1] = 1
  else:
    final_list[0] = i + 100
    final_list[1] = 0

  return final_list

# Input a and b values, as well as initial x_0
a = 0
b = 15
initial = 1.1

print(f"x_0 = {initial}", "f(x_0) = ", f(initial))

# Initialization
y = initial
x = [initial, 0]
k = 0
error_num = 0.00001 # How accruate you want it to be

# While loop that runs the code
while abs(f(x[k+1]) - f(x[k])) >= error_num:
  x[k] = y

  if fxx(x[k]) > 0:
    x.append(x[k] - (fx(x[k]))/(fxx(x[k])))

    # Choose Lambda
    lmbd = 0.01
    found = 0
    lmbd_list = [lmbd, found]
    while found == 0:
      lmbd_list = lambdatest(lmbd, x[k], x[k+1], a, b)
      lmbd = lmbd_list[0]
      found = lmbd_list[1]
      if lmbd <= 0:
        lmbd = 0.0001
        found = 1
    y = x[k] + lmbd*(x[k+1] - x[k])

  else:
    if fx(x[k]) >= 0:
      delta = -1

    else:
      delta = 1

    # Choose i
    i = 100
    found2 = 0
    i_list = [i,found2]
    while found2 == 0:
      i_list = itest(i, x[k], x[k+1], delta)
      i = i_list[0]
      found2 = i_list[1]

    # Choose lambda
    lmbd = 0.001
    found = 0
    lmbd_list = [lmbd, found]
    while found == 0:
      lmbd_list = lambdatest(lmbd, x[k], x[k+1], a, b)
      lmbd = lmbd_list[0]
      found = lmbd_list[1]
      if lmbd <= 0:
        lmbd = 0.0001
        found = 1
    y = x[k] + lmbd*(x[k+1]- x[k])
  k += 1

print(f"x_final = {round(x[k+1], 6)}, f(x_final) = {f(x[k+1])}")