import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

x = sp.symbols('x')
y = sp.Function('y')

ode = sp.Eq(y(x).diff(x), -2 * y(x)) 
ics = {y(0): sp.sqrt(2)} 

sympy_solution = sp.dsolve(ode, y(x), ics=ics)
y_sympy = sympy_solution.rhs 
print(f"Символьное решение: y(x) = {y_sympy}")

def ode_func(t, y):
    return -2 * y

y0 = [np.sqrt(2)]
t_span = (0, 10)
t_eval = np.linspace(*t_span, 500)

scipy_solution = solve_ivp(ode_func, t_span, y0, t_eval=t_eval)
t_values = scipy_solution.t
y_scipy = scipy_solution.y[0]

y_sympy_func = np.array([float(y_sympy.subs(x, t).evalf()) for t in t_values])

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t_values, y_sympy_func, label='SymPy Solution', color='blue')
plt.plot(t_values, y_scipy, label='SciPy Solution', linestyle='dashed', color='red')
plt.title('Решения дифференциального уравнения')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t_values, y_sympy_func - y_scipy, label='Разница (SymPy - SciPy)', color='green')
plt.title('Разница между решениями SymPy и SciPy')
plt.xlabel('x')
plt.ylabel('Разница')
plt.legend()
plt.grid()

plt.show()

