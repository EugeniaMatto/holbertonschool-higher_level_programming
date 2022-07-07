-- SQL
SELECT ge.name as genre, COUNT(sh_ge.genre_id) as number_of_shows
FROM tv_genres ge JOIN tv_show_genres sh_ge
ON
	ge.id = sh_ge.genre_id
GROUP BY ge.name
ORDER BY COUNT(sh_ge.genre_id) DESC;
