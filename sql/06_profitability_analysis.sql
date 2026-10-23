-- SQL dialect: PostgreSQL
SELECT "Category", "Segment", SUM("Sales") AS sales, SUM("Profit") AS profit,
       CASE WHEN SUM("Sales") = 0 THEN NULL ELSE SUM("Profit") / SUM("Sales") END AS profit_margin
FROM superstore_orders
GROUP BY "Category", "Segment"
ORDER BY profit_margin DESC;
