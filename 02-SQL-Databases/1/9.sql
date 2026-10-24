CREATE TABLE Book (
    book_id INT PRIMARY KEY,
    title NVARCHAR(100),
    author NVARCHAR(50),
    published_year INT
);

CREATE TABLE Member (
    member_id INT PRIMARY KEY,
    name NVARCHAR(50),
    email NVARCHAR(50),
    phone_number NVARCHAR(20)
);

CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    return_date DATE NULL,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES Book(book_id),
    CONSTRAINT fk_member FOREIGN KEY (member_id) REFERENCES Member(member_id)
);
GO
