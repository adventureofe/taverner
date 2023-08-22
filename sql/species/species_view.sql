DROP VIEW IF EXISTS vw_species;
CREATE VIEW vw_species AS
SELECT
    s.id,
    s.name,
    e1.name as fav_element_1,
    e2.name as fav_element_2,
    s.weight_min,
    s.weight_max,
    s.length_min,
    s.length_max,
    s.rarity
FROM species AS s
INNER JOIN element AS e1 ON fav_element_1 = e1.id
INNER JOIN element AS e2 ON fav_element_2 = e2.id;

DROP VIEW IF EXISTS vw_species_property;
CREATE VIEW vw_species_property AS
SELECT
    sp.id,
    sp.name
FROM species_property AS sp;

DROP VIEW IF EXISTS vw_species_property_entry;
CREATE VIEW vw_species_property_entry AS
SELECT
    spe.species AS id,
    s.name,
    spe.species_property AS id,
    sp.name
FROM species_property_entry AS spe
INNER JOIN species AS s ON spe.species = s.id
INNER JOIN species_property as sp ON spe.species_property = sp.id;
