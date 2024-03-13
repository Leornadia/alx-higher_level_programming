-- Script to list all the cities of California in the database 'hbtn_0d_usa'

-- Select the id and name of cities
SELECT cities.id, cities.name
FROM cities
-- Join with the states table using a subquery
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name = 'California'
)
-- Order the results by cities.id in ascending order
ORDER BY cities.id ASC;
