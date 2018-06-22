-- Assignment: MySQL Countries
-- Karen Clark
-- 2018-06-21

-- Queries
-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
SELECT countries.name, languages.language, languages.percentage 
FROM languages
JOIN countries ON languages.country_id = countries.id
where languages.language = 'Slovene' 
ORDER BY languages.percentage DESC ;

-- 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
SELECT countries.name, count(distinct(cities.id)) AS `city_count` 
FROM countries
JOIN cities ON countries.id = cities.country_id 
GROUP BY countries.name
ORDER BY city_count DESC;

-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)
SELECT name, populatiON FROM cities 
where populatiON > 500000 
AND cities.country_id = (SELECT countries.id FROM countries where name = "Mexico") 
ORDER BY populatiON DESC;

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
SELECT countries.name, languages.language, languages.percentage 
FROM languages 
JOIN countries ON languages.country_id = countries.id 
where percentage > 89.0 
GROUP BY countries.name 
ORDER BY percentage DESC;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT countries.name 
FROM countries 
where surface_area < 501 
AND populatiON > 100000;

-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
SELECT name 
FROM countries 
where government_form = "CONstitutiONal MONarchy" 
AND capital > 200 
AND life_expectancy > 75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
SELECT countries.name, cities.name, cities.district, cities.populatiON
FROM countries
JOIN cities ON countries.id = cities.country_id
where countries.name = "Argentina"
AND cities.district = "Buenos Aires"
AND cities.populatiON > 500000;

-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
SELECT regiom, count(distinct(id)) AS `country_count`
FROM countries
GROUP BY regiON
ORDER BY country_count DESC;