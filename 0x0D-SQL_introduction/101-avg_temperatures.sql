-- Display the acerage temperature
SELECT city,
AVG(value) AS avg_tmp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
