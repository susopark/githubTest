-- SQL Query to find the top-selling products in each category
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