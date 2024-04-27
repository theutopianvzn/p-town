-- Create tables
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    City VARCHAR(50),
    Country VARCHAR(50)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);

CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert sample data
INSERT INTO Customers (CustomerID, CustomerName, City, Country)
VALUES
    (1, 'John Doe', 'New York', 'USA'),
    (2, 'Jane Smith', 'London', 'UK'),
    (3, 'Michael Johnson', 'Paris', 'France');

INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES
    (1, 1, '2023-04-01'),
    (2, 1, '2023-04-15'),
    (3, 2, '2023-04-20'),
    (4, 3, '2023-04-25');

INSERT INTO Products (ProductID, ProductName, Price)
VALUES
    (1, 'Product A', 10.99),
    (2, 'Product B', 15.99),
    (3, 'Product C', 20.99);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES
    (1, 1, 2),
    (1, 2, 3),
    (2, 3, 1),
    (3, 1, 4),
    (4, 2, 2);

-- Nested subquery in the SELECT clause
SELECT
    CustomerName,
    (SELECT COUNT(*) FROM Orders WHERE Orders.CustomerID = Customers.CustomerID) AS OrderCount
FROM
    Customers;

-- Nested subquery in the WHERE clause
SELECT
    ProductName,
    Price
FROM
    Products
WHERE
    ProductID IN (
        SELECT ProductID
        FROM OrderDetails
        WHERE Quantity > 2
    );

-- Nested subquery in the FROM clause
SELECT
    CustomerName,
    OrderDate,
    TotalAmount
FROM
    (
        SELECT
            Customers.CustomerName,
            Orders.OrderDate,
            SUM(OrderDetails.Quantity * Products.Price) AS TotalAmount
        FROM
            Customers
            JOIN Orders ON Customers.CustomerID = Orders.CustomerID
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            JOIN Products ON OrderDetails.ProductID = Products.ProductID
        GROUP BY
            Customers.CustomerName,
            Orders.OrderDate
    ) AS OrderSummary
WHERE
    TotalAmount > 30;

-- Correlated subquery
SELECT
    CustomerName,
    (
        SELECT
            COUNT(*)
        FROM
            Orders
        WHERE
            Orders.CustomerID = Customers.CustomerID
    ) AS OrderCount
FROM
    Customers;