DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments(
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

CREATE TABLE Employees(
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentID INT NULL,
    Salary DECIMAL(10,2)
);

CREATE TABLE Projects(
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(50),
    EmployeeID INT NULL
);

SELECT e.EmployeeID,e.Name,d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID;


SELECT e.EmployeeID,e.Name,d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID=d.DepartmentID;


SELECT e.EmployeeID,e.Name,d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.DepartmentID=d.DepartmentID;


SELECT e.EmployeeID,e.Name,d.DepartmentName
FROM Employees e
FULL OUTER JOIN Departments d ON e.DepartmentID=d.DepartmentID;


SELECT d.DepartmentName,SUM(e.Salary) AS TotalSalary
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
GROUP BY d.DepartmentName;


SELECT d.DepartmentName,p.ProjectName
FROM Departments d
CROSS JOIN Projects p;


SELECT e.EmployeeID,e.Name,d.DepartmentName,p.ProjectName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID=d.DepartmentID
LEFT JOIN Projects p ON e.EmployeeID=p.EmployeeID;
