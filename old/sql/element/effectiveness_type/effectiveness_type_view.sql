DROP VIEW IF EXISTS vw_effectiveness_type;
CREATE VIEW vw_effectiveness_type AS
SELECT
    e_t.id,
    e_t.name
FROM effectiveness_type as e_t;
