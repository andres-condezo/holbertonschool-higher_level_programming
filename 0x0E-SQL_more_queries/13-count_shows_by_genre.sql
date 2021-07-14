-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS "number_of_shows"
FROM tv_show_genres
ORDER BY number_of_shows DESC;
INNER JOIN tv_genres
ON tv_show_genres.gender_id = tv_genres.id
GROUP BY tv_show_genres.genrer.id
