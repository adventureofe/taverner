.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP VIEW IF EXISTS vw_item;
CREATE VIEW vw_item AS
SELECT
    i.id,
    i.name,
    d.name AS diet,
    c.name AS colour,
    i.description AS description
FROM item AS i
INNER JOIN diet AS d on diet = d.id
INNER JOIN colour AS c ON colour = c.id;

