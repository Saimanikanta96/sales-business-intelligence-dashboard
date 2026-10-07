-- SQL dialect: PostgreSQL-style identifiers
-- Sample Superstore: executive sales overview
SELECT COUNT(*) AS line_items,
       COUNT(DISTINCT "Order ID") AS orders,
       COUNT(DISTINCT "Customer ID") AS customers,
       COUNT(DISTINCT "Product ID") AS products,
       SUM("Sales") AS total_sales,
       SUM("Profit") AS total_profit,
       AVG("Sales") AS avg_line_sales
FROM superstore_orders;
