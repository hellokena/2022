select sum(city.population)
from city, country
where countrycode = country.code and continent = 'asia'
