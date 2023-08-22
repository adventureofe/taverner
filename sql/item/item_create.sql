--you can recieve food from a party member that dies of a certain species

.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP TABLE IF EXISTS diet;
CREATE TABLE diet
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS item;
CREATE TABLE item
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    diet INTEGER NOT NULL,
    FOREIGN KEY(diet) REFERENCES diet(id)
);
