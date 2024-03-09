DROP VIEW IF EXISTS vw_element;
CREATE VIEW vw_element AS
SELECT
    e.id,
    e.name,
    et.name as type,
    c.name as colour,
    e.describer
FROM element AS e
INNER JOIN element_type AS et ON type = et.id
INNER JOIN  vw_element_score_small AS es ON e.id = es.id
INNER JOIN colour AS c ON colour = c.id;
