DROP TABLE IF EXISTS test_identity;

CREATE TABLE test_identity(
    ID INT IDENTITY,
    name VARCHAR(50)
);

INSERT INTO test_identity(name) VALUES ('A'), ('B'), ('C'), ('D'), ('E');
SELECT * FROM test_identity;


DELETE FROM test_identity;
SELECT * FROM test_identity;


TRUNCATE TABLE test_identity;
SELECT * FROM test_identity;

DROP TABLE IF EXISTS test_identity;