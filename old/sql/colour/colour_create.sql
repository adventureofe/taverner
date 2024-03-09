DROP TABLE IF EXISTS colour_simile_type;
CREATE TABlE colour_simile_type
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);


DROP TABLE IF EXISTS colour;
CREATE TABLE colour
(
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL CHECK(length(name) <= 64),
       r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
       g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
       b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255),
       describer TEXT NOT NULL CHECK(length(describer) <= 64),
       simile TEXT NOT NULL CHECK(length(simile) <= 64),
       simile_type INTEGER NOT NULL,
       FOREIGN KEY(simile_type) REFERENCES colour_simile_type(id)
);

CREATE TRIGGER check_color_simile_type
BEFORE INSERT ON colour
FOR EACH ROW
WHEN NEW.simile_type > (SELECT COUNT(*) FROM colour_simile_type) OR NEW.simile_type < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN colour_create.sql: INVALID simile_type VALUE');
END;
