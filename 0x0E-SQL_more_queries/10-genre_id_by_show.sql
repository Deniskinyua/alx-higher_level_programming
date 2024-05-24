-- Import dump : hbtn_0d_tvshows (/hbtn_0d_tvshows)
-- List all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Each record should displaye: tv_shows.title, tv_show_genre.genre_id
-- sorted in ASC by tv_shows.title & tv_show_genres.genre_id
-- ONLY 1 SELECT statement
-- DB passed as args
SELECT tv_shows.title, tvg.genre_id 
FROM tv_shows 
INNER JOIN tv_show_genres AS tvg
ON tv_shows.id = tvg.show_id
ORDER BY tv_shows.title, tvg.genre_id;
