import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

with open('C:/Users/LEGION/Downloads/100.txt', 'r') as f:
    lines = f.readlines()
N = int(lines[0].strip())
A = np.array([list(map(float, lines[i + 1].split())) for i in range(N)])
b = np.array(list(map(float, lines[N + 1].split())))

x = solve(A, b)
    
plt.bar(range(len(x)), x)
plt.xlabel('Индекс переменной')
plt.ylabel('Значение')
plt.title('Решение системы линейных уравнений')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

