DROP TABLE IF EXISTS TestMax;
CREATE TABLE TestMax
(
    Year1 INT,
    Max1 INT,
    Max2 INT,
    Max3 INT
);
GO

INSERT INTO TestMax 
VALUES
    (2001,10,101,87),
    (2002,103,19,88),
    (2003,21,23,89),
    (2004,27,28,91);

SELECT 
    Year1,
    CASE 
        WHEN Max1 >= Max2 AND Max1 >= Max3 THEN Max1
        WHEN Max2 >= Max1 AND Max2 >= Max3 THEN Max2
        ELSE Max3
    END AS MaxValue
FROM TestMax;
GO