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
  name TEXT NOT NULL CHECK(length(name) <= 64),
  fav_element_1 INTEGER NOT NULL,
  fav_element_2 INTEGER NOT NULL,
  colour INTEGER NOT NULL,
  weight_min INTEGER NOT NULL CHECK(weight_min > 0),
  weight_max INTEGER NOT NULL CHECK(weight_max > 0),
  length_min INTEGER NOT NULL CHECK(length_min > 0),
  length_max INTEGER NOT NULL CHECK(length_max > 0),
  rarity INTEGER NOT NULL CHECK(rarity > 0),
  hp INTEGER NOT NULL CHECK(hp > 0),
  atk INTEGER NOT NULL CHECK(atk > 0),
  def INTEGER NOT NULL CHECK(def > 0),
  sp_atk INTEGER NOT NULL CHECK(sp_atk > 0),
  sp_def INTEGER NOT NULL CHECK(sp_def > 0),
  speed INTEGER NOT NULL CHECK(speed > 0),
  base_stat_total INTEGER GENERATED ALWAYS AS (hp + atk + def + sp_atk + sp_def + speed) STORED,
  FOREIGN KEY(fav_element_1) REFERENCES element(id),	
  FOREIGN KEY(fav_element_2) REFERENCES element(id),
  FOREIGN KEY(colour) REFERENCES colour(id)
);

CREATE TRIGGER update_base_stat_total
AFTER UPDATE OF hp, atk, def, sp_atk, sp_def, speed, base_stat_total ON species
FOR EACH ROW
BEGIN
    UPDATE species
    SET base_stat_total = NEW.hp + NEW.atk + NEW.def + NEW.sp_atk + NEW.sp_def + NEW.speed
    WHERE id = NEW.id AND NEW.base_stat_total <> OLD.base_stat_total;
END;

DROP TABLE IF EXISTS species_property;
CREATE TABLE species_property
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);

DROP TABLE IF EXISTS species_property_entry;
CREATE TABLE species_property_entry
(
    species INTEGER NOT NULL,
    species_property INTEGER NOT NULL,
    PRIMARY KEY (species, species_property)
);

CREATE TRIGGER check_species_favourite_type_1
BEFORE INSERT ON species
FOR EACH ROW
WHEN NEW.fav_element_1 > (SELECT COUNT(*) FROM element) OR NEW.fav_element_1 < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN species_create.sql: INVALID fav_element_1 VALUE');
END;

CREATE TRIGGER check_species_colour
BEFORE INSERT ON species
FOR EACH ROW
WHEN NEW.colour > (SELECT COUNT(*) FROM colour) OR NEW.colour < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN species_create.sql: INVALID colour VALUE');
END;


CREATE TRIGGER check_species_favourite_type_2
BEFORE INSERT ON species
FOR EACH ROW
WHEN NEW.fav_element_2 > (SELECT COUNT(*) FROM element) OR NEW.fav_element_2 < 1
BEGIN
   SELECT RAISE(FAIL, 'ERROR IN species_create.sql: INVALID fav_element_2 VALUE');
END;
