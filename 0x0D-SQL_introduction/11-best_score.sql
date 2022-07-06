-- SQL
SELECT * FROM (
SELECT score, name FROM second_table ORDER BY score DESC)
WHERE
	score >= 10;
