DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS #EmployeeTransfers;

CREATE TABLE Employees(
    EmployeesID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(50),
    Department NVARCHAR(50),
    Salary INT
);

INSERT INTO Employees(Name, Department, Salary)
VALUES
    ('Alice', 'HR', 5000),
    ('Bob', 'IT', 7000),
    ('Charlie', 'Sales', 6000),
    ('David', 'HR', 5500),
    ('Emma', 'IT', 7200);

CREATE TABLE #EmployeeTransfers(
    EmployeesID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(50),
    Department NVARCHAR(50),
    Salary INT
);

INSERT INTO #EmployeeTransfers (Name, Department, Salary)
SELECT Name,
       CASE Department
           WHEN 'HR' THEN 'IT'
           WHEN 'IT' THEN 'Sales'
           WHEN 'Sales' THEN 'HR'
       END AS Department,
       Salary
FROM Employees;

SELECT * FROM #EmployeeTransfers;
