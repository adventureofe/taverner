.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP VIEW IF EXISTS vw_move;
CREATE VIEW vw_move AS
SELECT
    m.id,
    m.name,
    e.name as element,
    mt.name as type,
    m.priority,
    ma.name as ai_prompt,
    mc.name as category,
    me.name as effect,
    m.chance
FROM move AS m
INNER JOIN element AS e ON element = e.id
INNER JOIN move_type AS mt ON m.type = mt.id
INNER JOIN move_category as mc ON m.category = mc.id
INNER JOIN move_ai_prompt as ma ON m.ai_prompt = ma.id
INNER JOIN move_effect AS me ON m.effect = me.id;

DROP VIEW IF EXISTS vw_move_physical;
CREATE VIEW vw_move_physical AS
SELECT *
FROM vw_move
WHERE type = 'physical';

DROP VIEW IF EXISTS vw_move_special;
CREATE VIEW vw_move_special AS
SELECT *
FROM vw_move
WHERE type = 'special';
