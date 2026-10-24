CREATE TABLE account (
    account_id INT PRIMARY KEY,
    balance DECIMAL(10,2) CHECK (balance >= 0),
    account_type NVARCHAR(20) CHECK (account_type IN ('Saving','Checking'))
);
GO

ALTER TABLE account
ADD CONSTRAINT chk_balance CHECK (balance >= 0);
GO

