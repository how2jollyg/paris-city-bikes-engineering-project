---Counting the duplicated rows--- 
SELECT
(SELECT COUNT(1)
FROM (SELECT DISTINCT * 
			FROM `city-bikes-project-403113.city_bikes.fact_table`))as distinct_rows,
(SELECT COUNT(1) 
FROM (SELECT *
			FROM `city-bikes-project-403113.city_bikes.fact_table` ))as total_rows;

---Showing duplicated rows---
SELECT station_id,last_reported
FROM `city-bikes-project-403113.city_bikes.fact_table`
GROUP BY 1,2
HAVING COUNT(*) > 1;

--Replace Table Query--
CREATE OR REPLACE TABLE `city_bikes.fact_table`
AS (
  SELECT DISTINCT * 
  FROM `city_bikes.fact_table`
)