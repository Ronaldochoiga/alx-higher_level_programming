-- lists all the records of second_table where name is not NULL ordered by score
SELECT DISTINCT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
