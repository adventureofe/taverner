DROP TABLE IF EXISTS element;
CREATE TABLE element
(
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL CHECK(length(name) <= 64),
       type INTEGER NOT NULL,
       colour INTEGER NOT NULL,
       describer TEXT NOT NULL CHECK(length(describer) <= 64),
       FOREIGN KEY(type) REFERENCES element_type(id),
       FOREIGN KEY(colour) REFERENCES colour(id)
);

CREATE TRIGGER check_element_type
BEFORE INSERT ON element
FOR EACH ROW
WHEN NEW.type > (SELECT COUNT(*) FROM element_type) OR NEW.type < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN element_create.sql: INVALID element_type VALUE');
END;

CREATE TRIGGER check_element_colour
BEFORE INSERT ON element
FOR EACH ROW
WHEN NEW.colour > (SELECT COUNT(*) FROM colour) OR NEW.colour < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN element_create.sql: INVALID colour VALUE');
END;
