# 1. Why do you think companies analyze large volumes of data?
# Companies analyze large datasets to better understand customer behavior, 
# discover patterns and trends, improve decision-making, optimize resources, 
# increase efficiency, and gain a competitive advantage in the market.

# 2. If analyzing and sorting large data manually in Excel is difficult, 
# how do you think Python can help solve this problem?
# Python can automate repetitive tasks, handle millions of rows of data efficiently, 
# and provide powerful libraries such as Pandas and NumPy for data manipulation. 
# With Python, tasks that are nearly impossible in Excel can be done within seconds.

# Example:
import pandas as pd
import numpy as np

# Create a large dataset
data = pd.DataFrame({
    "CustomerID": np.arange(1, 10001),
    "PurchaseAmount": np.random.randint(10, 1000, 10000)
})

# Sort customers by their spending
sorted_data = data.sort_values(by="PurchaseAmount", ascending=False)
print("Top 5 biggest spenders:\n", sorted_data.head())

# 3. Imagine you work at a sales company that receives 
# data about 10,000 customer transactions daily. 
# How would you analyze this data?
# I would import the data into a Pandas DataFrame, clean and preprocess it,
# then calculate key metrics such as total revenue, most purchased products, 
# customer frequency, and generate daily/weekly reports.

# Example:
daily_transactions = pd.DataFrame({
    "CustomerID": np.random.randint(1, 2000, 10000),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones"], 10000),
    "Amount": np.random.randint(50, 2000, 10000)
})

# Analyze total sales per product
sales_summary = daily_transactions.groupby("Product")["Amount"].sum()
print("\nDaily sales summary by product:\n", sales_summary)

# 4. In your opinion, what tasks can Python be useful for in BI processes?
# Python can be very useful for:
# - Data Cleaning (handling missing or incorrect values)
# - Data Transformation and Integration (combining multiple sources)
# - Data Visualization (matplotlib, seaborn, plotly)
# - Predictive Analytics (machine learning models using scikit-learn)
# - Automated Reporting and Dashboards

# Example: Simple visualization
import matplotlib.pyplot as plt

sales_summary.plot(kind="bar", title="Sales by Product")
plt.ylabel("Total Sales")
plt.show()

# 5. If you wanted to compare a company's profit year by year, 
# how could this be done using Python?
# I would load the company's financial data into a DataFrame, 
# group the data by year, calculate the total profit per year, 
# and then visualize it to show trends.

# Example:
profit_data = pd.DataFrame({
    "Year": [2021, 2021, 2022, 2022, 2023, 2023],
    "Profit": [5000, 7000, 8000, 6000, 10000, 12000]
})

yearly_profit = profit_data.groupby("Year")["Profit"].sum()
print("\nYearly profit comparison:\n", yearly_profit)

yearly_profit.plot(kind="line", marker="o", title="Yearly Profit Trend")
plt.ylabel("Profit ($)")
plt.show()

# 6. If you don't know Python, what difficulties might you face 
# when working with large datasets?
# - Manual processing becomes very time-consuming and error-prone.
# - Tools like Excel cannot efficiently handle millions of rows.
# - Limited scalability and automation.
# - Inability to apply advanced analytics, machine learning, or automation techniques.
