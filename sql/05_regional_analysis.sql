-- Regional and geographic performance
SELECT
    [Region], [State], [City],
    SUM([Sales]) AS sales,
    SUM([Profit]) AS profit,
    COUNT(DISTINCT [Order ID]) AS orders,
    COUNT(DISTINCT [Customer ID]) AS customers
FROM superstore_orders
GROUP BY [Region], [State], [City]
ORDER BY sales DESC;
