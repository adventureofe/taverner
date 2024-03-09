.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files
-- taverner.sql is the main sql file

DROP TABLE IF EXISTS name_gender;
CREATE TABLE name_gender
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);


DROP TABLE IF EXISTS name_type;
CREATE TABLE name_type
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);

DROP TABLE IF EXISTS name;
CREATE TABLE name
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    gender INTEGER NOT NULL,
    type INTEGER NOT NULL,
    FOREIGN KEY(gender) REFERENCES name_gender(id)
    FOREIGN KEY(type) REFERENCES name_type(id)
);

CREATE TRIGGER check_name_gender
BEFORE INSERT ON name
FOR EACH ROW
WHEN NEW.gender > (SELECT COUNT(*) FROM name_gender) OR NEW.gender< 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN name_create.sql: INVALID name_gender VALUE');
END;

CREATE TRIGGER check_name_type
BEFORE INSERT ON name
FOR EACH ROW
WHEN NEW.type > (SELECT COUNT(*) FROM name_type) OR NEW.type < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN name_create.sql: INVALID name_type VALUE');
END;
