import pandas as pd
file_path = 'C:/Users/LEGION/Downloads/transactions.csv'
data = pd.read_csv(file_path)

ok_transactions = data[data['STATUS'] == 'OK']
top_3_payments = ok_transactions.nlargest(3, 'SUM')

umbrella_total = ok_transactions[ok_transactions['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum()
top_3_payments, umbrella_total

print("Три самых крупных платежа (статус OK):")
print(top_3_payments)
print("\nОбщая сумма платежей в адрес 'Umbrella, Inc' (статус OK):", umbrella_total)
