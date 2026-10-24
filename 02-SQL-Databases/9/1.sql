DROP TABLE IF EXISTS Employees

CREATE TABLE Employees
(
	EmployeeID  INTEGER PRIMARY KEY,
	ManagerID   INTEGER NULL,
	JobTitle    VARCHAR(100) NOT NULL
);
INSERT INTO Employees (EmployeeID, ManagerID, JobTitle) 
VALUES
	(1001, NULL, 'President'),
	(2002, 1001, 'Director'),
	(3003, 1001, 'Office Manager'),
	(4004, 2002, 'Engineer'),
	(5005, 2002, 'Engineer'),
	(6006, 2002, 'Engineer');


SELECT * FROM Employees;

;WITH Factorial AS (
    SELECT 1 AS n, 1 AS fact
    UNION ALL
    SELECT n + 1, fact * (n + 1)
    FROM Factorial
    WHERE n < 10
)
SELECT n, fact AS Factorial FROM Factorial;

;WITH Fibonacci AS (
    SELECT 1 AS n, 1 AS fib, 0 AS prev
    UNION ALL
    SELECT n + 1, fib + prev, fib
    FROM Fibonacci
    WHERE n < 10
)
SELECT n, fib AS Fibonacci_Number FROM Fibonacci;


