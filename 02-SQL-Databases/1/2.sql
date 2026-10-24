CREATE TABLE product (
    product_id INT UNIQUE,
    product_name NVARCHAR(50),
    price DECIMAL(10,2)
);
GO

ALTER TABLE product
ADD CONSTRAINT uq_product UNIQUE (product_id);
GO

ALTER TABLE product
ADD CONSTRAINT uq_product_name UNIQUE (product_id, product_name);
GO


