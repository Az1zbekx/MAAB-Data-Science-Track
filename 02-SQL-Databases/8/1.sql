CREATE TABLE [dbo].[EMPLOYEES_N]
(
    [EMPLOYEE_ID] [int] NOT NULL,
    [FIRST_NAME] [varchar](20) NULL,
    [HIRE_DATE] [date] NOT NULL
);

WITH cte AS (
  SELECT [Step Number],[Status],
         ROW_NUMBER() OVER(ORDER BY [Step Number]) -
         ROW_NUMBER() OVER(PARTITION BY [Status] ORDER BY [Step Number]) AS grp
  FROM Groupings
)
SELECT MIN([Step Number]) AS [Min Step Number],
       MAX([Step Number]) AS [Max Step Number],
       [Status],
       COUNT(*) AS [Consecutive Count]
FROM cte
GROUP BY [Status],grp
ORDER BY MIN([Step Number]);


WITH years AS (
  SELECT y=1975 UNION ALL SELECT y FROM generate_series(1976,YEAR(GETDATE()),1)
),
hire_years AS (
  SELECT DISTINCT YEAR(HIRE_DATE) y FROM EMPLOYEES_N
),
missing AS (
  SELECT y FROM years WHERE y NOT IN (SELECT y FROM hire_years)
),
grp AS (
  SELECT y,
         y - ROW_NUMBER() OVER(ORDER BY y) AS grp
  FROM missing
)
SELECT CAST(MIN(y) AS VARCHAR(4)) + ' - ' + CAST(MAX(y) AS VARCHAR(4)) AS [Years]
FROM grp
GROUP BY grp
ORDER BY MIN(y);


WITH years AS (
  SELECT 1975 AS y
  UNION ALL
  SELECT y + 1 FROM years WHERE y + 1 <= YEAR(GETDATE())
)
