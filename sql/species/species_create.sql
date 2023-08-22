.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP TABLE IF EXISTS species;
CREATE TABLE species
(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  fav_element_1 INTEGER NOT NULL,
  fav_element_2 INTEGER NOT NULL,
  weight_min INTEGER NOT NULL,
  weight_max INTEGER NOT NULL,
  length_min INTEGER NOT NULL,
  length_max INTEGER NOT NULL,
  rarity INTEGER NOT NULL
);

DROP TABLE IF EXISTS species_property;
CREATE TABLE species_property
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS species_property_entry;
CREATE TABLE species_property_entry
(
    species INTEGER NOT NULL,
    species_property INTEGER NOT NULL,
    PRIMARY KEY (species, species_property)
);
