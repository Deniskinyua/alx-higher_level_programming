-- Import hbtn_0c_0 this table dump -> /temperatures
-- Display the avergae temp (Fahrenheit) by city ordered by temperatures (descending)
SELECT CITY, AVG(VALUE) AS AVERAGE_TEMP FROM TEMPERATURES GROUP BY CITY ORDER BY AVERAGE_TEMP DESC;
