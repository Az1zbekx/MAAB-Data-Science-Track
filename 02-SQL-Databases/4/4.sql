DROP TABLE IF EXISTS letters;
CREATE TABLE letters
(
    letter CHAR(1)
);
GO

INSERT INTO letters
VALUES ('a'), ('a'), ('a'), 
  ('b'), ('c'), ('d'), ('e'), ('f');


SELECT letter
FROM letters
ORDER BY 
    CASE WHEN letter = 'b' THEN 0 ELSE 1 END,
    letter;


SELECT letter
FROM letters
ORDER BY 
    CASE WHEN letter = 'b' THEN 1 ELSE 0 END,
    letter;


SELECT letter
FROM letters
ORDER BY 
    CASE 
        WHEN letter = 'b' THEN 3 
        WHEN letter < 'b' THEN 1 
        ELSE 2 
    END;
GO