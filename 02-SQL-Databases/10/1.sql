DROP TABLE IF EXISTS Shipments;

CREATE TABLE Shipments (
    N INT PRIMARY KEY,
    Num INT
);

INSERT INTO Shipments (N, Num) VALUES
(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
(9,2),(10,2),(11,2),(12,2),(13,2),
(14,4),(15,4),(16,4),(17,4),(18,4),(19,4),(20,4),(21,4),(22,4),(23,4),(24,4),(25,4),
(26,5),(27,5),(28,5),(29,5),(30,5),(31,5),
(32,6),(33,7);

WITH AllDays AS (
    SELECT Num FROM Shipments
    UNION ALL
    SELECT 0 AS Num FROM (SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7) AS Missing
),
Ordered AS (
    SELECT Num, ROW_NUMBER() OVER (ORDER BY Num) AS rn
    FROM AllDays
)
SELECT AVG(Num*1.0) AS Median
FROM Ordered
WHERE rn IN (20, 21);
