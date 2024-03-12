-- Display top 3 cities by temperature during July and August, ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM weather
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

