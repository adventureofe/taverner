.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP VIEW IF EXISTS vw_name;
CREATE VIEW vw_name AS
SELECT
    n.id,
    n.name,
    ng.name AS gender,
    nt.name AS type
FROM name AS n
INNER JOIN name_gender AS ng ON n.gender = ng.id
INNER JOIN name_type AS nt ON n.type = nt.id;

DROP VIEW IF EXISTS vw_name_count;
CREATE VIEW vw_name_count AS
SELECT
    SUM(CASE WHEN gender = 'male' THEN 1 ELSE 0 END) as male_names,
    SUM(CASE WHEN gender = 'female' THEN 1 ELSE 0 END) as female_names,
    SUM(CASE WHEN gender = 'genderless' THEN 1 ELSE 0 END) as genderless_names
FROM vw_name;
