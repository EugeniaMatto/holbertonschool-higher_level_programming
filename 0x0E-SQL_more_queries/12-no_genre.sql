-- SQL
SELECT sh.title, sh_ge.genre_id
FROM tv_shows sh LEFT JOIN tv_show_genres sh_ge
ON
	sh.id = sh_ge.show_id
WHERE sh_ge.show_id IS NULL
ORDER BY sh.title, sh_ge.genre_id;
