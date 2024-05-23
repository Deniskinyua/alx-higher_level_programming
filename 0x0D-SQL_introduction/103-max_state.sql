-- Import /temperatures
-- Display max temp of @ state (ORDERED BY state name)
SELECT STATE, MAX(VALUE) AS MAXIMUM_TEMP FROM temperatures GROUP BY STATE ORDER BY STATE;
