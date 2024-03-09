DROP VIEW IF EXISTS vw_colour;
CREATE VIEW vw_colour AS
SELECT
    c.id,
    c.name,
    c.r,
    c.g,
    c.b,
    c.describer,
    cst.name as simile_type,
    c.simile
FROM colour AS c
INNER JOIN colour_simile_type AS cst ON simile_type = cst.id;
