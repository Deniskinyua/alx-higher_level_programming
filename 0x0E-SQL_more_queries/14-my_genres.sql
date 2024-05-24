-- Task 14
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres AS tvg ON tv_genres.id = tvg.genre_id 
INNER JOIN tv_shows  ON tv_shows.id = tvg.show_id WHERE tv_shows = "Dexter" ORDER BY tv_genres.name;
