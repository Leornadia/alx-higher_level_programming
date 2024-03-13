-- List all Comedy shows
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres_shows ON tv_shows.id = tv_genres_shows.tv_show_id
JOIN tv_genres ON tv_genres_shows.tv_genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

