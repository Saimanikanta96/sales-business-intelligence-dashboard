-- SQL dialect: PostgreSQL
-- This measures observed association; it does not establish causality.
SELECT CASE WHEN "Discount" = 0 THEN '0%'
            WHEN "Discount" <= 0.10 THEN '1-10%'
            WHEN "Discount" <= 0.20 THEN '11-20%'
            WHEN "Discount" <= 0.30 THEN '21-30%'
            WHEN "Discount" <= 0.50 THEN '31-50%'
            ELSE '51%+' END AS discount_band,
       COUNT(*) AS line_items, SUM("Sales") AS sales, SUM("Profit") AS profit
FROM superstore_orders
GROUP BY 1 ORDER BY 1;
