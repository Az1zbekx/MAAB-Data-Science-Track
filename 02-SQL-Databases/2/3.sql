DROP TABLE IF EXISTS photos;

CREATE TABLE photos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    image_data VARBINARY(MAX)
);

INSERT INTO photos (image_data)
SELECT * FROM OPENROWSET(BULK N'/home/kali/Pictures/test.jpg', SINGLE_BLOB) AS ImageSource;
