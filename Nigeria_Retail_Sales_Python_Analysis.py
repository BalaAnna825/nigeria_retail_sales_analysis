# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:33:50 2026

@author: USER
"""



import pandas as pd
data = pd.read_csv(r"C:\Users\USER\Desktop\Nigeria_Retail_Sales_600_Rows.csv 11.csv")

print(data.head(5))

print(data.shape)
print(data.columns)
print(data.isnull().sum())

import pandas as pd
df = pd.DataFrame(data)
import pandas as pd
import numpy as np

# Convert calculation columns to numeric
cols = ['Quantity', 'UnitPrice_NGN', 'UnitCost_NGN', 'DiscountRate']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Identify invalid values
df.loc[df['Quantity'] < 0, 'Quantity'] = np.nan
df.loc[df['UnitPrice_NGN'] < 0, 'UnitPrice_NGN'] = np.nan
df.loc[df['UnitCost_NGN'] < 0, 'UnitCost_NGN'] = np.nan
df.loc[~df['DiscountRate'].between(0, 1), 'DiscountRate'] = np.nan

# Gross Revenue
data['GrossRevenue'] = data['Quantity'] * data['UnitPrice_NGN']

# Net Revenue
data['NetRevenue'] = data['GrossRevenue'] * (1 - data['DiscountRate'])

# Total Cost
data['TotalCost'] = data['Quantity'] * data['UnitCost_NGN']

# Profit
data['Profit'] = data['NetRevenue'] - data['TotalCost']

# Profit Margin (%)
data['Profit Margin'] = np.where(
    data['NetRevenue'] != 0,
    (data['Profit'] / data['NetRevenue']) * 100,
    np.nan
)

# Display calculated columns
print(data[['GrossRevenue', 'NetRevenue',
          'TotalCost', 'Profit', 'Profit Margin']])

print(data.groupby('Product')['NetRevenue'].sum().sort_values(ascending=False))
 
print(data.groupby('Region')['Profit'].sum().sort_values(ascending=False))

total_NetRevenue = data['NetRevenue'].sum()
Total_Cost = data['TotalCost'].sum()
Total_Profit = data['Profit'].sum()
print("total_NetRevenue:",total_NetRevenue)
print("Total_Cost:",Total_Cost)
print("Total_Profit:",Total_Profit)

import pandas as pd
import matplotlib.pyplot as plt

# Convert OrderDate to datetime format
data['OrderDate'] = pd.to_datetime(data['OrderDate'], errors='coerce')

monthly_revenue = (
    data.dropna(subset=['OrderDate'])
      .set_index('OrderDate')
      .resample('ME')['NetRevenue']
      .sum()
)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker='o',
    linewidth=2
)
ax.set_xlabel('Month')
ax.set_ylabel('Net Revenue (NGN)')
ax.set_title('Monthly Net Revenue Trend')
ax.tick_params(axis='x', labelrotation=45)
fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
profit_by_product = data.groupby('Product')['Profit'].sum()

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(profit_by_product.index, profit_by_product.values)
ax.set_xlabel('Product')
ax.set_ylabel('Total Profit (NGN)')
ax.set_title('Total Profit by Product')
ax.tick_params(axis='x', labelrotation=45)
fig.tight_layout()
plt.show()