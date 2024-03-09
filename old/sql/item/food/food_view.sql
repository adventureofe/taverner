DROP VIEW IF EXISTS vw_food;
CREATE VIEW vw_food AS
SELECT
    f.id,
    f.name,
    f.rarity,
    f.price,
    c.name as colour
FROM food AS f
INNER JOIN colour AS c ON colour = c.id;
