import pandas as pd 

df = pd.read_csv('orders.csv')
print(df)

print('length before droping', len(df))
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

print(df.dtypes)
print('Dropping Rows: ')
print(df[(df['price'].isna()) | (df['qty'].isna())])
df = df.dropna(subset=['price', 'qty'])

print('length after droping', len(df))

df['revenue'] = df['price'] * df['qty']
print(f"Total Revenue = {df['revenue'].sum()}")
print('Revenue Per Channel', df.groupby('channel')['revenue'].sum())
print(df)


df.to_excel("clean_orders.xlsx", index=False)
back = pd.read_excel("clean_orders.xlsx")
print(back)
print(back.dtypes)