CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name NVARCHAR(50),
    order_date DATE
);
GO

ALTER TABLE orders
ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);
GO

