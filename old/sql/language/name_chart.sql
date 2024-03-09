SELECT gender, COUNT(*) AS gender_count
FROM name
GROUP BY gender;

SELECT type, COUNT(*) AS type_count
FROM name
GROUP BY type;
