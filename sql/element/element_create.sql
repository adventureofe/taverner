DROP TABLE IF EXISTS element;
CREATE TABLE element
(
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       type INTEGER NOT NULL,
       colour INTEGER NOT NULL,
       FOREIGN KEY(type) REFERENCES element_type(id),
       FOREIGN KEY(colour) REFERENCES colour(id)
);

CREATE TRIGGER check_element_type
BEFORE INSERT ON element
FOR EACH ROW
WHEN NEW.type > (SELECT COUNT(*) FROM element_type) OR NEW.type < 1
BEGIN
    SELECT RAISE(FAIL, 'INVALID TYPE VALUE');
END;

CREATE TRIGGER check_element_colour
BEFORE INSERT ON element
FOR EACH ROW
WHEN NEW.colour > (SELECT COUNT(*) FROM colour) OR NEW.colour < 1
BEGIN
    SELECT RAISE(FAIL, 'INVALID COLOUR VALUE');
END;
