-- lists all the cities of California
-- sorted in ascending
SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY id ASC;
