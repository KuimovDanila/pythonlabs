import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

initial_state = np.loadtxt("C:/Users/LEGION/Downloads/start dat.txt")

n = len(initial_state)

A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 1  
    A[i, (i + 1) % n] = -1 

time_steps = 255

u = np.zeros((time_steps, n))
u[0] = initial_state 

for t in range(1, time_steps):
    u[t] = u[t - 1] - 0.5 * (A @ u[t - 1]) 

fig, ax = plt.subplots(figsize=(12, 8))
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, n - 1)
ax.set_ylim(np.min(u), np.max(u))
ax.set_title("Эволюция функции u(x) во времени")
ax.set_xlabel("x")
ax.set_ylabel("u(x)")
ax.grid()

def update(frame):
    line.set_data(np.arange(n), u[frame])
    ax.set_title(f"Шаг {frame}")
    return line,

ani = FuncAnimation(fig, update, frames=time_steps, blit=True)

writer = PillowWriter(fps=20)
ani.save("C:/Users/LEGION/Downloads/evolution.gif", writer=writer)

plt.show()
