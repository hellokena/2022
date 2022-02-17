-- WHERE something LIKE ('bla%', '%foo%', 'batz%') 불가

SELECT distinct(CITY)
FROM STATION
WHERE CITY LIKE 'A%' OR
      CITY LIKE 'E%' OR
      CITY LIKE 'I%' OR
      CITY LIKE 'O%' OR
      CITY LIKE 'U%';
