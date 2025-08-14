import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# SQL query to summarize sales by product
query = '''
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(amount) AS total_revenue
FROM sales
GROUP BY product
'''

# Load query result into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close database connection
conn.close()

# Print the sales summary
print("Sales Summary:")
print(df)

# Plot revenue by product
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['total_revenue'])
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.title('Revenue by Product')
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig('sales_chart.png')
plt.show()
