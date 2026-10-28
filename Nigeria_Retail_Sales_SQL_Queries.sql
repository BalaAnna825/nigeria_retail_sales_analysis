CREATE TABLE nigeria_retail_sales (
OrderID VARCHAR(50),
OrderDate DATE,
CustomerType VARCHAR(50),
State VARCHAR(100),
City VARCHAR(100),
Region VARCHAR(100),
SalesChannel VARCHAR(50),
PaymentMethod VARCHAR(50),
Product VARCHAR(100),
Category VARCHAR(100),
Quantity INTEGER,
UnitPrice_NGN NUMERIC(14,2),
UnitCost_NGN NUMERIC(14,2),
DiscountRate NUMERIC(6,4),
SalesRep VARCHAR(100),
OrderStatus VARCHAR(30),
GrossRevenue NUMERIC(14,2),
NetRevenue NUMERIC(14,2),
TotalCost NUMERIC(14,2),
Profit NUMERIC(14,2)
);

SELECT * FROM retail_sales

SELECT COUNT(*)
FROM retail_sales

SELECT
   product,
    SUM("netrevenue") AS total_net_revenue,
    SUM("profit") AS total_profit
FROM retail_sales
GROUP BY "product";

SELECT
DATE_TRUNC('month', "orderdate") AS sales_month,
SUM("netrevenue") AS total_net_revenue
FROM retail_sales
WHERE "orderdate" >= '2025-01-01'
AND "orderdate" < '2026-01-01'
GROUP BY DATE_TRUNC('month', "orderdate")
ORDER BY sales_month ASC;


SELECT CITY,
SUM("netrevenue") AS total_netrevenue
FROM retail_sales
WHERE "orderstatus" <>'cancelled'
GROUP BY "city"
ORDER BY SUM("netrevenue") DESC
LIMIT(5);


SELECT saleschannel,
AVG("netrevenue") AS Average_NetRevenue
FROM retail_sales
GROUP BY "saleschannel"
ORDER BY Average_netrevenue DESC;


SELECT "product",
SUM("netrevenue") AS Total_netrevenue
FROM retail_sales
GROUP BY "product"
HAVING SUM("netrevenue")>5000000;



