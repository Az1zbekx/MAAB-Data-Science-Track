
DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees(
    EmployeeID INT IDENTITY(1,1),
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    HireDate DATE
);

SELECT Name, Department, Salary,
       ROW_NUMBER() OVER (ORDER BY Salary DESC) AS SalaryRank
FROM Employees;

SELECT Name, Department, Salary,
       RANK() OVER (ORDER BY Salary DESC) AS SalaryRank
FROM Employees;

SELECT *
FROM (
    SELECT Name, Department, Salary,
           RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS rnk
    FROM Employees
) AS t
WHERE rnk <= 2;

SELECT Name, Department, Salary
FROM (
    SELECT Name, Department, Salary,
           ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary ASC) AS rn
    FROM Employees
) AS t
WHERE rn = 1;


SELECT Name, Department, Salary,
       SUM(Salary) OVER (PARTITION BY Department ORDER BY HireDate) AS RunningTotal
FROM Employees;


SELECT Name, Department, Salary,
       SUM(Salary) OVER (PARTITION BY Department) AS TotalDeptSalary
FROM Employees;


SELECT Name, Department, Salary,
       AVG(Salary) OVER (PARTITION BY Department) AS AvgDeptSalary
FROM Employees;

SELECT Name, Department, Salary,
       Salary - AVG(Salary) OVER (PARTITION BY Department) AS DiffFromAvg
FROM Employees;


SELECT EmployeeID, Name, Salary,
       AVG(Salary) OVER (ORDER BY EmployeeID ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS MovingAvg
FROM Employees;

SELECT SUM(Salary) AS Last3HiredTotal
FROM (
    SELECT Salary
    FROM Employees
    ORDER BY HireDate DESC
    OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY
) AS t;

SELECT Name, Salary,
       AVG(Salary) OVER (ORDER BY HireDate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningAvg
FROM Employees;


SELECT EmployeeID, Name, Salary,
       MAX(Salary) OVER (ORDER BY EmployeeID ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS SlidingMax
FROM Employees;

SELECT Name, Department, Salary,
       CAST(Salary * 100.0 / SUM(Salary) OVER (PARTITION BY Department) AS DECIMAL(10,2)) AS PercentageContribution
FROM Employees;
