DROP VIEW IF EXISTS vw_element_type;
CREATE VIEW vw_element_type AS
SELECT
    e_t.id,
    e_t.name
FROM element_type AS e_t;
