CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_name NVARCHAR(50)
);

CREATE TABLE item (
    item_id INT PRIMARY KEY,
    item_name NVARCHAR(50),
    category_id INT,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category(category_id)
);
GO

ALTER TABLE item
ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category(category_id);
GO

