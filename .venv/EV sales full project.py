
#
# Objective: Analyzed global EV data (2010-2024) to explore trends in EV stock, sales, and market share.
# Tools: Python (Pandas, Seaborn, Matplotlib).
# Key Insights:
# Visualized EV stock share across regions and powertrain types.
# Analyzed EV sales share distribution, identifying growth patterns.
# Aggregated total EV sales by region and powertrain.
# Outcome: Identified significant regional differences and trends in EV adoption, aiding in market understanding.
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Define the file path
file_path = (r'C:\Users\Jitendra\PycharmProjects\pythonProject4\.venv\IEA Global EV Data 2024.csv')
# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

import os

# Verify the file path and existence of the file
print(f"Checking file at: {file_path}")
if os.path.isfile(file_path):
    print("File is found.")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content successfully read.")
            # Display the first 500 characters of the file
            print(content[:5000])
    except Exception as e:
        print(f"Error reading the file: {e}")
else:
    print("File does not exist at the specified path.")

# Handle missing values in the dataset
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Filter data for EV stock share
ev_stock_share = data[data['parameter'] == 'EV stock share']

# Plot the EV stock share distribution over the years
plt.figure(figsize=(12, 8))
sns.lineplot(data=ev_stock_share, x='year', y='value', hue='region', marker='o')
plt.title('EV Stock Share Distribution Over Years')
plt.xlabel('Year')
plt.ylabel('EV Stock Share (%)')
plt.legend(title='Region')
plt.grid(True)
plt.show()
#
# Reload the dataset for further analysis
df = pd.read_csv(file_path)
print(df.head())

# Filter data for EV sales share
ev_sales_share = data[data['parameter'] == 'EV sales share']

# Plot the EV sales share distribution over the years
plt.figure(figsize=(12, 8))
sns.lineplot(data=ev_sales_share, x='year', y='value', hue='region', marker='o')
plt.title('EV Sales Share Distribution Over Years')
plt.xlabel('Year')
plt.ylabel('EV Sales Share (%)')
plt.legend(title='Region')
plt.grid(True)
plt.show()

# Filter data for total EV sales
ev_sales = data[data['parameter'] == 'EV sales']

# Aggregate and plot total EV sales by region
total_ev_sales_by_region = ev_sales.groupby('region')['value'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
total_ev_sales_by_region.plot(kind='bar', color=plt.get_cmap('Set2').colors)
plt.title('Total EV Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total EV Sales (Vehicles)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()

# Filter data for EV stock
ev_stock = data[data['parameter'] == 'EV stock']

# Aggregate and plot EV stock by powertrain type
ev_stock_by_powertrain = ev_stock.groupby('powertrain')['value'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
ev_stock_by_powertrain.plot(kind='bar', color=plt.get_cmap('Paired').colors)
plt.title('EV Stock by Powertrain Type')
plt.xlabel('Powertrain Type')
plt.ylabel('EV Stock (Vehicles)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()

# Aggregate and plot EV sales share by region
ev_sales_share_by_region = ev_sales_share.groupby('region')['value'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
ev_sales_share_by_region.plot(kind='bar', color=plt.get_cmap('Set1').colors)
plt.title('EV Sales Share by Region')
plt.xlabel('Region')
plt.ylabel('Average EV Sales Share (%)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()

# Aggregate EV stock and sales by powertrain
ev_stock_by_powertrain = ev_stock.groupby('powertrain')['value'].sum()
ev_sales_by_powertrain = ev_sales.groupby('powertrain')['value'].sum()

# Plot EV stock and sales by powertrain
plt.figure(figsize=(14, 8))
plt.bar(ev_stock_by_powertrain.index, ev_stock_by_powertrain, color='lightblue', label='EV Stock')
plt.bar(ev_sales_by_powertrain.index, ev_sales_by_powertrain, color='lightcoral', alpha=0.7, label='EV Sales')
plt.title('EV Stock and Sales by Powertrain')
plt.xlabel('Powertrain Type')
plt.ylabel('Count')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()

# Plot the trend of EV stock share by powertrain over the years
plt.figure(figsize=(14, 8))
sns.lineplot(data=ev_stock_share, x='year', y='value', hue='powertrain', marker='o')
plt.title('Trend of EV Stock Share by Powertrain Over the Years')
plt.xlabel('Year')
plt.ylabel('EV Stock Share (%)')
plt.legend(title='Powertrain')
plt.grid(True)
plt.show()