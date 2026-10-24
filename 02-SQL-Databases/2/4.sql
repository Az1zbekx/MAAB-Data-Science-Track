DROP TABLE IF EXISTS student;

CREATE TABLE student (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50),
    classes INT,
    tuition_per_class DECIMAL(10,2),
    total_tuition AS (classes * tuition_per_class)
);

INSERT INTO student (name, classes, tuition_per_class)
VALUES
('Ali', 5, 100.00),
('Vali', 8, 90.50),
('Salim', 10, 120.00);

SELECT * FROM student;
