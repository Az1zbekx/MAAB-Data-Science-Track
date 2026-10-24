DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Products;


CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);


INSERT INTO Customers (CustomerID, CustomerName) VALUES
(1, 'Alice Johnson'),
(2, 'Bob Smith'),
(3, 'Charlie Brown'),
(4, 'Diana Prince'),
(5, 'Ethan Hunt'),
(6, 'Fiona Davis'),
(7, 'George Wilson'),
(8, 'Hannah Lee'),
(9, 'Ian Clark'),
(10, 'Julia Roberts');


INSERT INTO Products (ProductID, ProductName, Category) VALUES
(1, 'Laptop', 'Electronics'),
(2, 'Phone', 'Electronics'),
(3, 'Tablet', 'Electronics'),
(4, 'Headphones', 'Electronics'),
(5, 'Chair', 'Furniture'),
(6, 'Table', 'Furniture'),
(7, 'Notebook', 'Stationery'),
(8, 'Pen', 'Stationery'),
(9, 'Printer', 'Electronics'),
(10, 'Lamp', 'Furniture');


INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES
(101, 1, '2024-12-01'),
(102, 2, '2024-12-05'),
(103, 3, '2024-12-06'),
(104, 1, '2024-12-10'),
(105, 5, '2024-12-12'),
(106, 6, '2024-12-14'),
(107, 2, '2024-12-15'),
(108, 8, '2024-12-18'),
(109, 9, '2024-12-19'),
(110, 10, '2024-12-20');


INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity, Price) VALUES
(1, 101, 1, 1, 1500.00),
(2, 101, 4, 2, 200.00),
(3, 102, 2, 1, 800.00),
(4, 103, 5, 4, 120.00),
(5, 104, 7, 10, 5.00),
(6, 105, 3, 1, 600.00),
(7, 106, 9, 1, 1000.00),
(8, 107, 8, 20, 1.50),
(9, 108, 10, 2, 70.00),
(10, 109, 2, 1, 850.00),
(11, 109, 4, 1, 100.00),
(12, 110, 6, 1, 300.00),
(13, 110, 7, 5, 6.00),
(14, 105, 1, 1, 1500.00),
(15, 104, 8, 15, 2.00);

SELECT * FROM Customers;
SELECT * FROM OrderDetails;
SELECT * FROM Orders;
SELECT * FROM Products;

SELECT CustomerName, OrderID, OrderDate FROM Customers
LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;

SELECT CustomerName FROM Customers
LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE OrderID IS NULL;

SELECT Orders.OrderID, OrderDetails.Quantity, Products.ProductName
FROM Orders
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID;

SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS OrderCount
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName
HAVING COUNT(Orders.OrderID) > 1;

SELECT Orders.OrderID, MAX(OrderDetails.Price) AS MaxPrice FROM Orders
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
GROUP BY Orders.OrderID;

SELECT Customers.CustomerName, MAX(OrderDate) AS MaxOrderDate FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName;

SELECT Customers.CustomerName FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Customers.CustomerName
HAVING COUNT(DISTINCT CASE WHEN Products.Category <> 'Electronics' THEN Products.Category END) = 0;

SELECT Customers.CustomerName FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
WHERE Products.Category = 'Stationery'
GROUP BY Customers.CustomerName;

SELECT Customers.CustomerID, Customers.CustomerName, SUM(OrderDetails.Price * OrderDetails.Quantity) AS TotalSpent FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
GROUP BY Customers.CustomerID, Customers.CustomerName;











