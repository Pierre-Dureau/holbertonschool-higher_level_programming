-- lists all shows
-- with all their genres
SELECT tv_shows.title, tv_genres.name FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
