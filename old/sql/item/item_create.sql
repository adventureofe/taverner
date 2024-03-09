--you can recieve food from a party member that dies of a certain species

.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP TABLE IF EXISTS item_diet;
CREATE TABLE item_diet
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);

DROP TABLE IF EXISTS item;
CREATE TABLE item
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    diet INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(diet) REFERENCES item_diet(id),
    FOREIGN key(colour) REFERENCES colour(id)
);


CREATE TRIGGER check_item_diet
BEFORE INSERT ON item
FOR EACH ROW
WHEN NEW.diet > (SELECT COUNT(*) FROM item_diet) OR NEW.diet < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN item_create.sql: INVALID diet VALUE');
END;


CREATE TRIGGER check_item_colour
BEFORE INSERT ON item
FOR EACH ROW
WHEN NEW.colour > (SELECT COUNT(*) FROM colour) OR NEW.colour < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN item_create.sql: INVALID colour VALUE');
END;
