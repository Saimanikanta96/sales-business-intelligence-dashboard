-- Monthly sales and profit trend
SELECT
    EXTRACT(YEAR FROM [Order Date]) AS order_year,
    EXTRACT(MONTH FROM [Order Date]) AS order_month,
    SUM([Sales]) AS sales,
    SUM([Profit]) AS profit,
    COUNT(DISTINCT [Order ID]) AS orders
FROM superstore_orders
GROUP BY EXTRACT(YEAR FROM [Order Date]), EXTRACT(MONTH FROM [Order Date])
ORDER BY order_year, order_month;
