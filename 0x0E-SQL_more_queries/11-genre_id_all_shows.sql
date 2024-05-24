-- Genre ID for all shows
SELECT tv_shows.title, tsg.genre_id
FROM tv_shows
LEFT JOIN tv_show_genre AS tsg
ON tv_shows = tsg.show_id
ORDER BY tv_shows.title, tsg.genre_id;
