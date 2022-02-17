-- WHERE something LIKE ('bla%', '%foo%', 'batz%') 불가

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY LIKE 'A%' OR
      CITY LIKE 'E%' OR
      CITY LIKE 'I%' OR
      CITY LIKE 'O%' OR
      CITY LIKE 'U%';
      
SELECT DISTINCT(CITY)
FROM STATION
WHERE left(city,1) in ('a','e','i','o','u')
