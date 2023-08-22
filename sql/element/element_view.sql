DROP VIEW IF EXISTS vw_element;
CREATE VIEW vw_element AS
SELECT
    e.id,
    e.name,
    et.name as type,
    c.name as colour
FROM element as e
INNER JOIN element_type as et on e.type = et.id
INNER JOIN  vw_element_score_small as es on e.id = es.id
INNER JOIN colour as c on e.colour = c.id;
