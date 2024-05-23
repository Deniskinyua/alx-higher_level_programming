-- import in hbtn_0c_0 -> dump: /temperatures
-- Display the top 3 of cities temperature during July and August ordered by temp (DESC)
SELECT CITY, AVG(VALUE) AS AVERAGE_TEMP FROM temperatures WHERE MONTH = 7 OR MONTH = 8 GROUP BY CITY ORDER BY AVERAGE_TEMP DESC LIMIT 3;
