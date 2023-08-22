DROP VIEW IF EXISTS vw_colour;
CREATE VIEW vw_colour AS
SELECT
    c.id,
    c.name,
    c.r,
    c.g,
    c.b
FROM colour AS c;
