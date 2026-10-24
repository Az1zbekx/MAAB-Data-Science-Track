CREATE TABLE invoice (
    invoice_id INT IDENTITY(1,1),
    amount DECIMAL(10,2)
);
GO

INSERT INTO invoice (amount) VALUES (100), (200), (300), (400), (500);
GO

SET IDENTITY_INSERT invoice ON;
INSERT INTO invoice (invoice_id, amount) VALUES (100, 999);
SET IDENTITY_INSERT invoice OFF;
GO
