import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("C:/Users/LEGION/Downloads/signals/signals/signal03.dat")

filtered_data = np.zeros_like(data, dtype=float)

for i in range(len(data)):
    if i < 10:
        filtered_data[i] = np.mean(data[:i+1])
    else:
        filtered_data[i] = np.mean(data[i-9:i+1])

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(data, label='Raw Signal')
plt.title("Сырой сигнал")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(filtered_data, label='Filtered Signal')
plt.title("После фильтра")
plt.legend()
plt.show()
