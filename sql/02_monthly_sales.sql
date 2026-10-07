-- SQL dialect: PostgreSQL
SELECT DATE_TRUNC('month', "Order Date") AS month,
       SUM("Sales") AS sales,
       SUM("Profit") AS profit,
       COUNT(DISTINCT "Order ID") AS orders
FROM superstore_orders
GROUP BY 1 ORDER BY 1;
