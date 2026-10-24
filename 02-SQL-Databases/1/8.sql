CREATE TABLE books (
    book_id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price > 0),
    genre NVARCHAR(50) DEFAULT 'Unknown'
);
GO
