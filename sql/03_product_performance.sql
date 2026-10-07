-- Product and sub-category performance
SELECT
    [Category], [Sub-Category], [Product ID], [Product Name],
    SUM([Sales]) AS sales,
    SUM([Profit]) AS profit,
    SUM([Quantity]) AS quantity,
    COUNT(DISTINCT [Order ID]) AS orders
FROM superstore_orders
GROUP BY [Category], [Sub-Category], [Product ID], [Product Name]
ORDER BY sales DESC;
