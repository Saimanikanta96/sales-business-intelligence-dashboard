-- Customer contribution analysis
SELECT
    [Customer ID], [Customer Name], [Segment], [Region],
    SUM([Sales]) AS sales,
    SUM([Profit]) AS profit,
    COUNT(DISTINCT [Order ID]) AS orders
FROM superstore_orders
GROUP BY [Customer ID], [Customer Name], [Segment], [Region]
ORDER BY sales DESC;
