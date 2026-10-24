DROP TABLE IF EXISTS worker;

CREATE TABLE worker (
    id INT,
    name VARCHAR(50)
);

BULK INSERT worker
FROM '/home/az1zbekx/workers.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2, -- birinchi qatorda ustun nomlari bor
    FIELDTERMINATOR = ',', -- maydonlar vergul bilan ajratilgan
    ROWTERMINATOR = '\n',  -- har bir satr yangi qatorda
    TABLOCK
);
