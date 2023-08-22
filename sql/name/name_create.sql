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
    name TEXT NOT NULL
);


DROP TABLE IF EXISTS name_type;
CREATE TABLE name_type
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS name;
CREATE TABLE name
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender INTEGER NOT NULL,
    type INTEGER NOT NULL,
    FOREIGN KEY(gender) REFERENCES name_gender(id)
    FOREIGN KEY(type) REFERENCES name_type(id)
);
