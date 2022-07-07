-- script that lists all the cities of California in database hbtn_0d_usa

SELECT id, name
FROM cities
WHERE
	name = 'California'
ORDER BY id ASC
