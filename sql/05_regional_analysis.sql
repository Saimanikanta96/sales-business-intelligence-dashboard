-- SQL dialect: PostgreSQL
SELECT "Region", "State/Province", "City",
       SUM("Sales") AS sales, SUM("Profit") AS profit,
       COUNT(DISTINCT "Order ID") AS orders,
       COUNT(DISTINCT "Customer ID") AS customers
FROM superstore_orders
GROUP BY "Region", "State/Province", "City"
ORDER BY sales DESC;
