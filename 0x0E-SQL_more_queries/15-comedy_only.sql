-- Task 15
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres AS tvg ON tv_shows.id = tvg.show_id
INNER JOIN tv_genres AS tv_gn ON tv_gn = tvg.genre_id WHERE tv_gn.name = "Comedy" ORDER BY tv_shows.title;
