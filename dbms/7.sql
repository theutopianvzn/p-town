-- Create a table
CREATE TABLE sales (
    id INT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10, 2)
);

-- Insert some data
INSERT INTO sales (id, product, quantity, price)
VALUES
    (1, 'Product A', 10, 9.99),
    (2, 'Product B', 5, 14.99),
    (3, 'Product A', 8, 9.99),
    (4, 'Product C', 3, 19.99),
    (5, 'Product B', 7, 14.99);

-- Average (AVG)
SELECT AVG(price) AS "Average Price"
FROM sales;

-- Count (COUNT)
SELECT COUNT(*) AS "Total Rows"
FROM sales;

SELECT COUNT(DISTINCT product) AS "Unique Products"
FROM sales;

-- Minimum (MIN)
SELECT MIN(price) AS "Minimum Price"
FROM sales;

-- Maximum (MAX)
SELECT MAX(price) AS "Maximum Price"
FROM sales;

-- Sum (SUM)
SELECT SUM(quantity) AS "Total Quantity"
FROM sales;

SELECT SUM(quantity * price) AS "Total Revenue"
FROM sales;