CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    name NVARCHAR(50),
    city NVARCHAR(50) DEFAULT 'Unknown'
);
GO

ALTER TABLE customer
ADD CONSTRAINT df_city DEFAULT 'Unknown' FOR city;
GO

