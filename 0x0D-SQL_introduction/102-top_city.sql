-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

-- SELECT city, value FROM temperatures WHERE month = 7 or month = 8 ORDER BY value LIMIT 3;

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;