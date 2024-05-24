-- Genre ID for all shows
SELECT tvs.title, tsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tsg
ON tvs = tsg.show_id
ORDER BY tvs.title, tsg.genre_id;
