-- Task 13
SELECT tv_gn.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tv_gn
INNER JOIN tv_show_genres AS tvg 
ON tv_gn.id = tvg.genre_id
GROUP BY tv_gn ORDER BY number_of_shows DESC;
