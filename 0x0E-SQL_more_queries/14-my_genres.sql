-- List all genres of the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
JOIN tv_genres_shows ON tv_genres.id = tv_genres_shows.tv_genre_id
JOIN tv_shows ON tv_genres_shows.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

