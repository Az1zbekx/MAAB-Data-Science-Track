DECLARE @Year INT = 2025;
DECLARE @Month INT = 10;

;WITH Dates AS (
    SELECT DATEFROMPARTS(@Year, @Month, 1) AS DateValue
    UNION ALL
    SELECT DATEADD(DAY, 1, DateValue)
    FROM Dates
    WHERE DATEADD(DAY, 1, DateValue) < DATEADD(MONTH, 1, DATEFROMPARTS(@Year, @Month, 1))
),
Weeks AS (
    SELECT
        DateValue,
        DATEPART(WEEK, DateValue) - DATEPART(WEEK, DATEFROMPARTS(@Year, @Month, 1)) + 1 AS WeekNum,
        DATEPART(WEEKDAY, DateValue) AS WeekDayNum
    FROM Dates
)
SELECT
    MAX(CASE WHEN WeekDayNum = 1 THEN DAY(DateValue) END) AS Sunday,
    MAX(CASE WHEN WeekDayNum = 2 THEN DAY(DateValue) END) AS Monday,
    MAX(CASE WHEN WeekDayNum = 3 THEN DAY(DateValue) END) AS Tuesday,
    MAX(CASE WHEN WeekDayNum = 4 THEN DAY(DateValue) END) AS Wednesday,
    MAX(CASE WHEN WeekDayNum = 5 THEN DAY(DateValue) END) AS Thursday,
    MAX(CASE WHEN WeekDayNum = 6 THEN DAY(DateValue) END) AS Friday,
    MAX(CASE WHEN WeekDayNum = 7 THEN DAY(DateValue) END) AS Saturday
FROM Weeks
GROUP BY WeekNum
ORDER BY WeekNum
OPTION (MAXRECURSION 1000);
