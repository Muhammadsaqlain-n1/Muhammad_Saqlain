import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\saqla\Downloads\Sample - Superstore.csv', encoding='latin1')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.columns = df.columns.str.replace(' ', '_')
df.head()

region_profit = df.groupby('Region')['Profit'].sum().reset_index()
sns.barplot(x='Region', y='Profit', data=region_profit)
plt.title('Total Profit By Region')
plt.show()

category_profit = df.groupby('Category')['Profit'].sum().reset_index()
sns.barplot(x='Category', y='Profit', data=category_profit)
plt.title('Profit by Category')
plt.show()

top_customers = df.groupby('Customer_Name')['Profit'].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind='barh')
plt.title('Top 10 Customers by Profit')
plt.xlabel('Profit')
plt.show()

pivot_table = df.pivot_table(values='Profit', index='Category', columns='Region', aggfunc='sum')
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu')
plt.title('Profit Heatmap(Category vs Region)')
plt.show()
