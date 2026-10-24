CREATE TABLE student (
    id INT,
    name NVARCHAR(50),
    age INT
);
GO

ALTER TABLE student
ALTER COLUMN id INT NOT NULL;
GO
