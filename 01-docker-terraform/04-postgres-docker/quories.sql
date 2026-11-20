-- Create a test table
CREATE TABLE test (
    id INTEGER,
    name VARCHAR(50)
);

-- Insert sample data
INSERT INTO test VALUES (1, 'Hello Docker');
INSERT INTO test VALUES (2, 'Data Engineering');
INSERT INTO test VALUES (3, 'PostgreSQL');

-- Retrieve all records
SELECT * FROM test;

-- Filter records
SELECT * FROM test
WHERE id > 1;

-- Select a specific column
SELECT name FROM test;

-- Count records
SELECT COUNT(*) FROM test;

-- Count filtered records
SELECT COUNT(*) FROM test
WHERE id > 1;