import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/LEGION/Downloads/flights.csv'
data = pd.read_csv(file_path)

df = pd.DataFrame(data)

result = df.groupby('CARGO').agg(
    flights=('CARGO', 'count'),
    total_price=('PRICE', 'sum'),
    total_weight=('WEIGHT', 'sum')
).reset_index()

print(result)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

result.plot(kind='bar', x='CARGO', y='total_weight', ax=ax1, color='b', position=0, width=0.4, label='Общий вес', alpha=0.7)

result.plot(kind='bar', x='CARGO', y='total_price', ax=ax2, color='r', position=1, width=0.4, label='Общая стоимость', alpha=0.7)

ax1.set_ylabel('Общий вес')
ax2.set_ylabel('Общая стоимость')
ax1.set_title('Грузы авиакомпаний')
fig.tight_layout() 
plt.show()
