-- Sales Business Intelligence
-- Expected table: sales
-- Canonical fields: order_id, order_date, sales, profit

SELECT
    COUNT(*) AS rows_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) / NULLIF(COUNT(DISTINCT order_id), 0) AS average_order_value
FROM sales;

SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS revenue,
    SUM(profit) AS profit
FROM sales
GROUP BY 1
ORDER BY 1;

SELECT category, SUM(sales) AS revenue, SUM(profit) AS profit
FROM sales
GROUP BY category
ORDER BY revenue DESC;

SELECT region, SUM(sales) AS revenue, SUM(profit) AS profit
FROM sales
GROUP BY region
ORDER BY revenue DESC;

SELECT product_name, SUM(sales) AS revenue, SUM(profit) AS profit
FROM sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;
