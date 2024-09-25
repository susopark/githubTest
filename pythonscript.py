import sqlite3  # For connecting to an SQLite database
import pandas as pd
from scipy.optimize import minimize  # To perform optimization

# Connect to SQLite database (you can use any database connection)
conn = sqlite3.connect('sales.db')

# Run the SQL query and load the data into a pandas DataFrame
query = """
    WITH CategoryRank AS (
        SELECT 
            product_id,
            category,
            quantity_sold,
            ROW_NUMBER() OVER (PARTITION BY category ORDER BY quantity_sold DESC) AS rank
        FROM sales
    )
    SELECT * 
    FROM CategoryRank 
    WHERE rank = 1;
"""
top_products = pd.read_sql_query(query, conn)

# Display the top-selling products
print("Top-selling products in each category:")
print(top_products)

# Example optimization: Minimize inventory holding costs

# Function to calculate total holding costs for each product based on the number of units
def holding_cost(units, holding_cost_per_unit=0.5):
    return holding_cost_per_unit * units

# Function to optimize the stock level for each top product
def optimize_inventory(row):
    # Minimize holding cost based on demand (quantity_sold)
    result = minimize(holding_cost, row['quantity_sold'], bounds=[(1, row['quantity_sold'] * 2)])
    return result.x  # Optimal number of units

# Apply optimization to the top products DataFrame
top_products['optimal_stock'] = top_products.apply(optimize_inventory, axis=1)

# Show the results
print("\nOptimized stock levels for top-selling products:")
print(top_products[['product_id', 'category', 'quantity_sold', 'optimal_stock']])

# Close the database connection
conn.close()