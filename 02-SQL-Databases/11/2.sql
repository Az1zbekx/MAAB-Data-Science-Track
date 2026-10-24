DROP TABLE IF EXISTS Orders_DB1;
DROP TABLE IF EXISTS Orders_DB2;


CREATE TABLE Orders_DB1(
    OrderID INT PRIMARY KEY,
    CustomerName NVARCHAR(50),
    Product NVARCHAR(50),
    Quantity INT
);


INSERT INTO Orders_DB1(OrderID, CustomerName, Product, Quantity)
VALUES
    (101, 'Alice', 'Laptop', 1),
    (102, 'Bob', 'Phone', 2),
    (103, 'Charlie', 'Tablet', 1),
    (104, 'David', 'Monitor', 1);


SELECT * FROM Orders_DB1;

CREATE TABLE Orders_DB2(
    OrderID INT PRIMARY KEY,
    CustomerName NVARCHAR(50),
    Product NVARCHAR(50),
    Quantity INT        
);

INSERT INTO Orders_DB2(OrderID, CustomerName, Product, Quantity)
VALUES
    (101, 'Alice', 'Laptop', 1),
    (103, 'Charlie', 'Tablet', 1);

SELECT * FROM Orders_DB2;

DECLARE @MissingOrders TABLE(
    OrderID INT PRIMARY KEY,
    CustomerName NVARCHAR(50),
    Product NVARCHAR(50),
    Quantity INT 
);


INSERT INTO @MissingOrders
SELECT *
FROM Orders_DB1 
WHERE OrderID NOT IN (SELECT OrderID FROM Orders_DB2);

SELECT * FROM @MissingOrders;

