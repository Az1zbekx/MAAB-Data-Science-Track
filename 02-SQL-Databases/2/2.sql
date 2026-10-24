DROP TABLE IF EXISTS data_types_demo;

CREATE TABLE data_types_demo(
    id INT,
    name VARCHAR(50),
    price DECIMAL(10, 2),
    quantity FLOAT,
    birth_date DATE,
    created_at DATETIME,
    is_active BIT,
    description NVARCHAR(50)
);

INSERT INTO data_types_demo
VALUES
(1, 'A', 1111.11, 1.1, '2005-05-10', GETDATE(), 1, 'O‘quvchi A'),
(2, 'B', 2222.22, 2.2, '2004-03-12', GETDATE(), 0, 'Talaba B'),
(3, 'C', 3333.33, 3.3, '2003-01-01', GETDATE(), 1, 'Xodim C');

SELECT * FROM data_types_demo;