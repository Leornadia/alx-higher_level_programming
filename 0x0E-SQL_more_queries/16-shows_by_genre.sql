-- List all shows and their associated genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres_shows ON tv_shows.id = tv_genres_shows.tv_show_id
LEFT JOIN tv_genres ON tv_genres_shows.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
