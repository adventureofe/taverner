DROP VIEW IF EXISTS vw_element_combinations;
CREATE VIEW vw_element_combinations AS
SELECT
    ef.attacker AS atk,
    e1.name AS attacker,
    ef.defender AS def,
    e2.name AS defender,
    et.name AS effectiveness
FROM element_effectiveness AS ef
INNER JOIN element AS e1 ON ef.attacker = e1.id
INNER JOIN element AS e2 ON ef.defender = e2.id
INNER JOIN effectiveness_type AS et ON et.id = ef.effectiveness;

DROP VIEW IF EXISTS vw_element_small;
CREATE VIEW vw_element_small AS
SELECT *
FROM vw_element_combinations
WHERE effectiveness != 'neutral';

DROP VIEW IF EXISTS vw_element_atk;
CREATE VIEW vw_element_atk AS
SELECT
    atk,
    attacker,
    -SUM(CASE WHEN effectiveness = 'weak' THEN 1 ELSE 0 END) AS atk_w,
    SUM(CASE WHEN effectiveness = 'neutral' THEN 1 ELSE 0 END) AS atk_n,
    SUM(CASE WHEN effectiveness = 'strong' THEN 1 ELSE 0 END) AS atk_s
FROM vw_element_combinations
GROUP BY atk;

DROP VIEW IF EXISTS vw_element_def;
CREATE VIEW vw_element_def AS
SELECT
    def,
    defender,
    SUM(CASE WHEN effectiveness = 'weak' THEN 1 ELSE 0 END) AS def_w,
    SUM(CASE WHEN effectiveness = 'neutral' THEN 1 ELSE 0 END) AS def_n,
    -SUM(CASE WHEN effectiveness = 'strong' THEN 1 ELSE 0 END) AS def_s
FROM vw_element_combinations
GROUP BY def;

DROP VIEW IF EXISTS vw_element_score;
CREATE VIEW vw_element_score AS
SELECT
    a.atk AS id,
    a.attacker AS name,
    a.atk_w,
    a.atk_s,
    (a.atk_s + a.atk_w) AS atk_score,
    d.def_w,
    d.def_s,
    (d.def_w + d.def_s) AS def_score,
    ((a.atk_s + a.atk_w) + (d.def_w + d.def_s)) AS total_score
FROM vw_element_atk AS a
INNER JOIN vw_element_def AS d ON a.atk = d.def;

DROP VIEW IF EXISTS vw_element_score_small;
CREATE VIEW vw_element_score_small AS
SELECT
    id,
    name,
    atk_score AS atk,
    def_score AS def,
    total_score AS total
FROM vw_element_score;
