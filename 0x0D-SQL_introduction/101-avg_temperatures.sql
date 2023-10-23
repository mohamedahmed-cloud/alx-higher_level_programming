-- Import in hbtn_0c_0 database this table dump: download

-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) from temperatures GROUP BY city ORDER BY AVG(value) DESC;