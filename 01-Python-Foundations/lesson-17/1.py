import sqlite3
import pandas as pd

# 1. Load the database
conn = sqlite3.connect('chinook.db')

# 2. Read customers and invoices tables
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

# 3. Perform inner join on CustomerId
merged = pd.merge(customers, invoices, on='CustomerId', how='inner')

# 4. Find total number of invoices per customer
invoice_counts = merged.groupby('CustomerId').size().reset_index(name='InvoiceCount')

print(invoice_counts.head())
