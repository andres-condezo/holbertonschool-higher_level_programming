-- a script that lists all shows contained in the database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows_genres
RIGHT JOIN tv_show
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
