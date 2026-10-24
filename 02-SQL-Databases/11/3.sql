DROP TABLE IF EXISTS WorkLog;

CREATE TABLE WorkLog(
    EmployeeID INT,
    EmployeeName NVARCHAR(50),
    Department NVARCHAR(50),
    WorkDate DATE,
    HoursWorked INT
);

INSERT INTO WorkLog(EmployeeID, EmployeeName, Department, WorkDate, HoursWorked)
VALUES
    (1, 'Alice', 'HR', '2024-03-01', 8),
    (2, 'Bob', 'IT', '2024-03-01', 9),
    (3, 'Charlie', 'Sales', '2024-03-02', 7),
    (1, 'Alice', 'HR', '2024-03-03', 6),
    (2, 'Bob', 'IT', '2024-03-03', 8),
    (3, 'Charlie', 'Sales', '2024-03-04', 9);

DROP VIEW IF EXISTS vw_MonthlyWorkSummary;

CREATE VIEW vw_MonthlyWorkSummary AS
SELECT 
    EmployeeID,
    EmployeeName,
    Department,
    SUM(HoursWorked) AS TotalHoursWorked,
    SUM(SUM(HoursWorked)) OVER(PARTITION BY Department) AS TotalHoursDepartment,
    AVG(SUM(HoursWorked)) OVER(PARTITION BY Department) AS AvgHoursDepartment
FROM WorkLog
GROUP BY EmployeeID, EmployeeName, Department;

SELECT * FROM vw_MonthlyWorkSummary;


